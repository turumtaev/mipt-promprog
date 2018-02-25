#!/usr/bin/env python3

from pymongo import MongoClient
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='hello')

base = MongoClient('mongodb://mongo:27017/')['hello']

def callback(ch, method, properties, body):
    base['messages'].insert({'message': body, 'queue': 'hello'})

channel.basic_consume(callback, queue='hello', no_ack=True)
channel.start_consuming()
