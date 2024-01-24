import pymongo

#connect to database
myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb= myclient["databasemongo"]
mycol= mydb["students"]

# Buscar objeto específico
myquery = { "address": "Highway 37" }

#Buscar el objeto especificando la variable query
mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
print("------------")
#Advanced Query
#To make advanced queries you can use modifiers as values in the query object.
myquery = { "address": { "$gt": "S" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)
print("------------")