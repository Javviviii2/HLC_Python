#Strings hacer "Nuevo" en mayúsculas
a = "CPIFP Nuevo (Desglose IES Campanilla)"
cpifp= a[:6]
nuevo= a[6:12]
desglose= a[12:]
print (cpifp + nuevo.upper() + desglose)

