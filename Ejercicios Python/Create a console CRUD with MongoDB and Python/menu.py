from functions import *

while True:
    clean_screen()
    
    print("\n"+"#"*5 + " MAIN MENU " + "#"*5)
    print(
    "\n"+
    "Select an option:"+"\n\n"+
    "1. Add Student"+"\n"+
    "2. Search Student"+"\n"+
    "3. Delete Student"+"\n"+
    "4. Modify Student"+"\n"+
    "5. Exit"+"\n"
    )
    option=int(input("Option: "))

    # Add student
    if option == 1:
        add_student()
        progretion()

    #Search student
    elif option == 2:
        print(search_student())
        progretion()

    # Delete student
    elif option == 3:
        delete_student()
        progretion()

    # Modify info
    elif option == 4:
        modify_student()
        progretion()

    # Exit
    elif option == 5:
        myclient.close()
        progretion()
        exit()
    else:
        print("Error, please choose one option.")
    
