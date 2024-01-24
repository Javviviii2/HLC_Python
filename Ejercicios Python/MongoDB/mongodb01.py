import pymongo

#connect to database
myclient=pymongo.MongoClient("mongodb://localhost:27017")

#crear database. Si no se añade registro no se crea
mydb= myclient["databasemongo"]

#crear colección (es el equivalente a tabla en mysql). Si no existe la crea
mycol= mydb["students"]

#insertar 1 dato. Se insertan los datos en modo diccionario
mydict={
    "name": "Javi",
    "ID": "1"
}

x=mycol.insert_one(mydict)

#muestra los ids insertados
print(x.inserted_ids)