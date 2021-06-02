import pika, json


params = pika.URLParameters('amqps://beehjujy:jFadcTP_7AP81_chiGUxw_YjhoFlNeT6@rat.rmq2.cloudamqp.com/beehjujy')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
	properties = pika.BasicProperties(method)
	channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)
