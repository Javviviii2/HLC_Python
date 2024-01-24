
# Se pasa un id y buscará ese id en la base de datos
def search(id):
    DataFilePath= "./students.txt"
    with open(DataFilePath, "r") as file:
        data= file.readlines()
    for line in data:
        if id in line:
            return line
    file.close()

#Guarda registro de acceso en archivo log
def log_register(id):
    import datetime
    log_file_path="access.log"
    with open(log_file_path, "a") as log:
        catch_time= datetime.datetime.now().strftime("%X")
        catch_date= datetime.datetime.now().strftime("%x")
        log.write("student id: "+ id +"\n"+ " "*5 + catch_time + " | " + catch_date + "\n")
        log.close()

#Registrar nuevo alumnado en la base de datos
def add_student():
        print("\n" + "Introduzca la información del estudiante => " + "\n")
        id= input("ID: ")
        
        #check id to avoid replication
        check_id(id)

        name= input("Nombre: ")
        surname = input("Apellidos: ")
        birthdate= input("Fecha de nacimiento (dd/mm/yyyy): ")
        print("\n" + "-"*30 + "\n")
        StudentInfo = [id,name, surname, birthdate]

        DataFilePath= "./students.txt"
        with open(DataFilePath,"a") as datafile:
            datafile.write (StudentInfo[0] + " | " + StudentInfo[1] + " | " + StudentInfo[2] + " | " + StudentInfo[3] + "\n")
            datafile.close()

#Check id para evitar duplicidades
def check_id (id):
    if id in str(search(id)):
        print("error, ID alredy exits. Try again?" +"\n" "To enter new data write (Y)" + "\n" + "To exit write (N)")
        error=input()
        if error.upper == "Y":
            add_student()
        else:
            exit()