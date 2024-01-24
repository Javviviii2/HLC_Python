import pymongo

myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb= myclient["databasemongo"]
mycol= mydb["students"]

#Ordenar por nombres
mydoc = mycol.find().sort("name")

for x in mydoc:
  print(x)

#Ordenar de manera descendente.
mydoc = mycol.find().sort("name", -1)

for x in mydoc:
  print(x)