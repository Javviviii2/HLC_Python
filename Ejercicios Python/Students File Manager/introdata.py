from functions import add_student

while True:
    ask_AddNewStudent=input("Add new student? Y or N: ")
    if ask_AddNewStudent.upper() == "Y":
        add_student()
    else:
        break