import pika, json

pikaURL = 'amqps://bxtgabcs:I_5pbVMUdP2Ryb2D5gUqLBOaOF5lNruu@beaver.rmq.cloudamqp.com/bxtgabcs'

params = pika.URLParameters(pikaURL)

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
