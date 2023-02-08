import pika, json
from app import create_app, db
from app.models import Product

app = create_app()
app.app_context().push()

pikaURL = 'amqps://bxtgabcs:I_5pbVMUdP2Ryb2D5gUqLBOaOF5lNruu@beaver.rmq.cloudamqp.com/bxtgabcs'

params = pika.URLParameters(pikaURL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')

def callback(ch, method, propertis, body):
    print("Recieve in main")
    data = json.loads(body)
    print(data)

    if propertis.content_type == 'product_created':
        product = Product(id=data['id'], title=data['title'], image=data['image'])
        with app.app_context():
            db.session.add(product)
            db.session.commit()
            print('Product created')

    elif propertis.content_type == 'product_updated':
        product = Product.query.get(data['id'])
        product.title = data['title']
        product.image = data['image']
        with app.app_context():
            db.session.commit()
            print('Product updated')

    elif propertis.content_type == 'product_deleted':
        product = Product.query.get(data)
        with app.app_context():
            db.session.delete(product)
            db.session.commit()
            print('Product deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print("Started consuming...")

channel.start_consuming()

channel.close()

