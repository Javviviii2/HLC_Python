import pymongo

#connect to database
myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb= myclient["databasemongo"]
mycol= mydb["students"]

#find_one() -- Devuelve el primer registro
x = mycol.find_one()

print(x)
print("------------")

#find() -- Devuelve todo
for x in mycol.find():
    print(x)
print("------------")

#Buscar campos específicos
# You are not allowed to specify both 0 and 1 values in the same object (except if one of the fields is the _id field). 
# If you specify a field with the value 0, all other fields get the value 1, and vice versa:
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)
print("------------")