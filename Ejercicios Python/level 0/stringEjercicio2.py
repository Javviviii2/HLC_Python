password = "aaaaaaaaaaaa"

#comprobar que la contraseña tiene un mínimo de 8 caracteres
#Comprobar que no tiene espacios en blanco

# Todo junto
if len(password) > 8:
    if " " in password:
        print("Error: espacios en blanco")
    else:
        print("Contraseña correcta")
else:
    print("Contraseña demasiado corta")

