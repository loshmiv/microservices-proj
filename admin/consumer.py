import pika, os, django
from product.models import Product

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

pikaURL = 'amqps://bxtgabcs:I_5pbVMUdP2Ryb2D5gUqLBOaOF5lNruu@beaver.rmq.cloudamqp.com/bxtgabcs'

params = pika.URLParameters(pikaURL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, propertis, body):
    print("Recieve in admin")
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=data)
    product.likes = product.likes + 1
    product.save()
    print("Product liked one more time.")


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
print("Started consuming...")

channel.start_consuming()

channel.close()
