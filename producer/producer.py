#!/usr/bin/env python3

import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='hello')
data = 'hello world'
channel.basic_publish(exchange='', routing_key='hello', body=data)
connection.close()