import pymongo

#connect to database
myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb= myclient["databasemongo"]
mycol= mydb["students"]

#insertar muchos datos
mylist =[
    {"name":"Pepe","ID":"2"},
    {"name":"Juan","ID":"3"},
]

x=mycol.insert_many(mylist)

#muestra los ids insertados
print(x.inserted_ids)