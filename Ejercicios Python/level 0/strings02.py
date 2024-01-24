a = "CPIFP Nuevo Desglose IES Campanilla"

if ("aaaa" in a):
    print ("ok")
else:
    print ("bad")

### strip()
email = "   asdasd@gmail.es   "
print (email.strip())

### replace()
print(a.replace("C", "D"))
print(a.replace("C", "D", 1)) #el número es cuantas veces reemplaza. Por ejemplo, 1 significa solo 1 vez

### split()
print(a.split(" ")) # le digo que usa como separador. Este caso: espacio en blanco. Devuelve array

a= a.split(" ")
for trozo in a:
    print(trozo)




