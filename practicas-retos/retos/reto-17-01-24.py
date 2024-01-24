# Crea un programa que simule el comportamiento del sombrero seleccionador del 
# universo mágico de Harry Potter.
# - De ser posible realizará 5 preguntas (como mínimo) a través de la terminal. 
# - Cada pregunta tendrá 4 respuestas posibles (también a selecciona una a través de terminal). 
# - En función de las respuestas a las 5 preguntas deberás diseñar un algoritmo que 
#   coloque al alumno en una de las 4 casas de Hogwarts (Gryffindor, Slytherin , Hufflepuff y Ravenclaw) 
# - Ten en cuenta los rasgos de cada casa para hacer las preguntas y crear el algoritmo seleccionador.
#
#  Por ejemplo, en Slytherin se premia la ambición y la astucia. 

import random

casas = {
    "Gryffindor": 0,
    "Hufflepuff": 0,
    "Ravenclaw": 0,
    "Slytherin": 0
}
# Creo una lista con el objeto PreguntaSombrero y dentro de cada uno
# una tupla con la pregunta y asociada a esta otra tupla con las respuestas 
preguntas = [
    ("¿Cómo te definirías?", [
        ("1. Valiente", "Gryffindor"),
        ("2. Leal", "Hufflepuff"),
        ("3. Sabio", "Ravenclaw"),
        ("4. Ambicioso", "Slytherin")
    ]),
    ("¿Cuál es tu clase favorita?", [
        ("1. Vuelo", "Gryffindor"),
        ("2. Pociones", "Ravenclaw"),
        ("3. Defensa contra las artes oscuras", "Slytherin"),
        ("4. Animales fantásticos", "Hufflepuff")
    ]),
    ("¿Dónde pasarías más tiempo?", [
        ("1. Invernadero", "Hufflepuff"),
        ("2. Biblioteca", "Ravenclaw"),
        ("3. En la sala común", "Slytherin"),
        ("4. Explorando", "Gryffindor")
    ]),
    ("¿Cuál es tu color favorito?", [
        ("1. Rojo", "Gryffindor"),
        ("2. Azul", "Ravenclaw"),
        ("3. Verde", "Slytherin"),
        ("4. Amarillo", "Hufflepuff")
    ]),
    ("¿Cuál es tu mascota?", [
        ("1. Sapo", "Ravenclaw"),
        ("2. Lechuza", "Gryffindor"),
        ("3. Gato", "Hufflepuff"),
        ("4. Serpiente", "Slytherin")
    ])
]

def respuesta_usuario():
    respuesta = input("Responde 1, 2, 3 o 4: ")
    if respuesta == "1" or respuesta == "2" or respuesta == "3" or respuesta == "4":
        return int(respuesta)
    else: # En caso de que no sea un número esperado, volver a preguntar
        return respuesta_usuario()    

print("Responde a las preguntas")

# Hacer las preguntas
for pregunta in preguntas: # imprimir la 1º pregunta
    print(pregunta[0])
    # para cada pregunta imprime las respuestas
    for respuestas in pregunta[1]:
        print(respuestas[0])
        
    casa = pregunta[1][respuesta_usuario()-1][1]
    casas[casa] += 1

seleccionar_casa = []
max_punto = 0

for casa, puntos in casas.items():
    if puntos > max_punto:
        seleccionar_casa.clear()
        seleccionar_casa.append(casa)
        max_punto = puntos
    elif puntos == max_punto:
        seleccionar_casa.append(casa)
        max_punto = puntos

print("Tu casa es: " + random.choice(seleccionar_casa))