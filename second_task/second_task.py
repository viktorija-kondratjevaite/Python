from pymongo import MongoClient


client = MongoClient()
database = client.database

# Parašykite užklausą atvaizduojančią visus dokumentus iš restoranų rinkinio
def f1():
    query = database.collection.find()
    for record in query:
        print(record)

# Parašykite užklausą, kuri atvaizduotų laukus - restaurant_id, name, borough ir cuisine - visiems dokumentams
def f2():
    query = database.collection.find({},{'restaurant_id' : 1, 'name' : 1, 'borough': 1, 'cuisine': 1})
    for record in query:
        print(record)

# Parašykite užklausą, kuri ayvaizduotų laukus - restaurant_id, name, borough ir cuisine -, bet nerodytų lauko field_id visiems dokumentams
def f3():
    query = database.collection.find({},{"_id": 0,'restaurant_id' : 1, 'name' : 1, 'borough': 1, 'cuisine': 1})
    for record in query:
        print(record)

# Parašykite užklausą, kuri parodytų visus miestelio Bronx restoranus
def f4():
    query = database.collection.find({'borough': "Bronx"})
    for record in query:
        print(record)

# Parašykite užklausą, kuri parodytų restoranus su įvertinimu tarp 80 ir 100.
def f5():
    query = database.collection.find({'grades': {'$elemMatch': {'score': {'$gte': 80, '$lte': 100 }}}})
    for record in query:
        print(record)