#!/usr/bin/env python3
from pymongo import MongoClient
db = MongoClient('mongodb://mongo:27018/')['hello']

res = list(db['messages'].find())
if len(res):
    for i, r in enumerate(res):
        print('Message %d: %s' % (i, r['message']))
else:
    print('[x] No items in promprog collection:(')