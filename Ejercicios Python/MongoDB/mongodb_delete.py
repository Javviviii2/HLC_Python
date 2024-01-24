import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb= myclient["databasemongo"]
mycol= mydb["students"]

#Borrar 1 objeto. Se hace primero 1 query
#myquery = { "address": "Mountain 21" }
#Ahora le digo borrar la query
#mycol.delete_one(myquery)

#Borrar varios objetos
#myquery = { "address": {"$regex": "^S"} }

#x = mycol.delete_many(myquery)

#Borrar todos los objetos de una colección
x = mycol.delete_many({})