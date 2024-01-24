from functions import search, log_register

while True:
    student_id=str(input("Please, introduce student ID: "))
    
    #log events
    log_register(student_id)
    
    #buscar información del estudiante
    print(search(student_id))
    ask = input("Find a new one? Y or N: ").upper()
    if ask != "Y":
        break