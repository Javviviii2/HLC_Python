nombre = "Javier"
apellidos = "Rodríguez Fernández"
dni = "77198220P"

# hacer el identificador de educaand

ape= apellidos.split(" ")
ape1=ape[0]
ape2=ape[1]
result= nombre[0] + ape1[:3] + ape2[:3] + dni[-4:-1]
ipasen= result.lower()
print(ipasen+"@e.educaand.es")