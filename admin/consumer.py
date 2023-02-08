import pika

pikaURL = 'amqps://bxtgabcs:I_5pbVMUdP2Ryb2D5gUqLBOaOF5lNruu@beaver.rmq.cloudamqp.com/bxtgabcs'

params = pika.URLParameters(pikaURL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, propertis, body):
    print("recieve in admin")
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)
print("Started consuming...")

channel.start_consuming()

channel.close()
