# 3. Imagen circular estilo mandala.
import random
import turtle
t = turtle.Turtle()
r = random
# Definimos el tamaño del mandala
radio = 100
# Velocidad
t.speed(0)
t.pensize(5)


def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    return turtle.color((R, G, B))


# Dibujar círculos
stop=0
while stop<random.randrange(20,100):
    for i in range (10):
        giro = 20
        t.right(giro+10)
        change_color()
        t.circle(radio)
    radio = radio+2
    stop +=1
    

# Mostramos el resultado
turtle.done()