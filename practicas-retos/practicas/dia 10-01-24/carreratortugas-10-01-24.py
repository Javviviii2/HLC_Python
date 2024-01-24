# 2. Crea una "carrera de tortugas" con al menos 2 jugadores. Para ello necesitarás dibujar 2 tortugas y que, aleatoriamente, se desplacen una cantidad entre 1 y 5 ud de desplazamiento. La primera en llegar al final de la pantalla será la ganadora.

import turtle
import random

# crear pantalla
turtle.Screen()

#crear objeto
jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()
 
#Crear jugadores
jugador1.hideturtle()
jugador1.shape("turtle")
jugador1.color("red","red") #color de la figura
jugador1.shapesize(2,2,2)
jugador1.pensize(3)
 
jugador2.hideturtle()
jugador2.shape("turtle")
jugador2.color("blue","blue") #color de la figura
jugador2.shapesize(2,2,2)
jugador2.pensize(3)
 
# crear la meta 
jugador1.penup()
jugador1.goto(200,200) # Posición de la meta
jugador1.pendown()
jugador1.goto(200,-300)

# colocando los jugadores en la posicion inicial
jugador1.penup()
jugador1.goto(-250,100)
jugador1.showturtle()

jugador2.penup()
jugador2.goto(-250,-170)
jugador2.showturtle()

# creacion del dado
dado = [1,2,3,4,5]

# movilizando jugadores
for i in range(20):
    # Comprobar quien gana
    if(jugador1.pos() >= (200,200)):
        print("Jugador rojo ha ganado")
        break
    elif(jugador2.pos() >= (200,-200)):
        print("Jugador azul ha ganado")
        break
    else:
        # turno del jugador1
        turno1 = random.choice(dado)
        jugador1.pendown()
        jugador1.forward(turno1*20)
        # turno del jugador2
        turno2 = random.choice(dado)
        jugador2.pendown()
        jugador2.forward(turno2*20)

turtle.done() 