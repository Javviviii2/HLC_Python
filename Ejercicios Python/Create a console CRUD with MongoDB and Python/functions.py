import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017")
mydb= myclient["databasemongo"]
mycol_students=mydb["students"]
mycol_logs=mydb["logs"]

# search student query on MongoDB
def search_student_query(student_id):
    student_id=int(student_id)
    return ({"ID": student_id})

# Añadir estudiante
def add_student():
        print("\n" + "Introduzca la información del estudiante => " + "\n")
        id= int(input("ID: "))
        name= input("Nombre: ")
        surname = input("Apellidos: ")
        birthdate= input("Fecha de nacimiento (dd/mm/yyyy): ")
        print("\n" + "-"*30 + "\n")
        studentinfo = {
            "ID" : id,
            "name" : name,
            "surname" : surname,
            "birthdate" : birthdate
        }
        mycol_students.insert_one(studentinfo)


# Se pasa un id y buscará ese id en la base de datos
def search_student():
    student_id=input("Select student ID: ")
    for register in mycol_students.find(search_student_query(student_id),{"_id":0}):
        return(register)

#Check id para evitar duplicidades

#Borrar estudiantes
def delete_student():
        student_id=input("Select student ID: ")
        mycol_students.delete_one(search_student_query(student_id))

# Modificar estudiante
def modify_student():
        student_id=input("Student ID to modify information: ")

        print(
        "\n"+
        "Which information do you want to update?"+"\n"+
        "1. ID"+"\n"+
        "2. Name"+"\n"+
        "3. Surname"+"\n"+
        "4. Birthdate"+"\n"+
        "5. Exit"+"\n"
        )
        update_data=int(input("Select Option: "))
        if update_data == 1:
            update_id=int(input("Insert new ID: "))
            update_id={"$set": {"ID":update_id}}
            mycol_students.update_one(search_student_query(student_id), update_id)
        elif update_data == 2:
            update_name=input("Insert new Name: ")
            update_name={"$set": {"name":update_name}}
            mycol_students.update_one(search_student_query(student_id), update_name)
        elif update_data == 3:
            update_surname=input("Insert new Surname: ")
            update_surname={"$set": {"name":update_surname}}
            mycol_students.update_one(search_student_query(student_id), update_surname)
        elif update_data == 4:
            update_birthdate=input("Insert new Birthdate: ")
            update_birthdate={"$set": {"name":update_birthdate}}
            mycol_students.update_one(search_student_query(student_id), update_birthdate)
        elif update_data == 5:
            progretion()
        else:
            print("Error")

# Dot waiting progretion
def progretion():
    import time, sys

    for i in range(5):
        time.sleep(.5)
        sys.stdout.write('.')
        sys.stdout.flush()
    clean_screen()

# Clean screen
def clean_screen():
    import os
    os.system('cls' if os.name=='nt' else 'clear')
