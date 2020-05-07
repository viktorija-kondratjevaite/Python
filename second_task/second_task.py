from pymongo import MongoClient


client = MongoClient()
database = client.database

def first():
    query = database.collection.find()
    for record in query:
        print(record)

def second():
    query = database.collection.find({},{'restaurant_id' : 1, 'name' : 1, 'borough': 1, 'cuisine': 1})
    for record in query:
        print(record)

def third():
    query = database.collection.find({},{"_id": 0,'restaurant_id' : 1, 'name' : 1, 'borough': 1, 'cuisine': 1})
    for record in query:
        print(record)

def fourth():
    query = database.collection.find({'borough': "Bronx"})
    for record in query:
        print(record)

def fift():
    query = database.collection.find({'grades': {'$elemMatch': {'score': {'$gte': 80, '$lte': 100 }}}})
    for record in query:
        print(record)