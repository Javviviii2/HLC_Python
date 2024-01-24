# 1. Dibuja tu nombre
# 2. Crea una "carrera de tortugas" con al menos 2 jugadores. Para ello necesitarás dibujar 2 tortugas y que, aleatoriamente, se desplacen una cantidad entre 1 y 5 ud de desplazamiento. La primera en llegar al final de la pantalla será la ganadora.
# 3. Imagen circular estilo mandala.
# 4. Espiral de fibonacci.

from turtle import *
# Definir resolución de la ventana de dibujo 
setup(640,480,0,0)
# Tamaño de zona de dibujo
screensize(300, 150)

# Tamaño pincel 
pensize(5)

#Dibujar letra J
goto(20,0)
penup()
goto(10,0)
pendown()
goto(10,-20)
goto(0,-10)
penup()

#Dibujar A
goto(40,-20)
pendown()
setx(40)
sety(0)
forward(20)
sety(-20)
penup()
goto(60,-10)
pendown()
back(20)
penup()

# Dibujar V
goto(90,0)
pendown()
goto(100,-20)
goto(110,0)
penup()

# Dibujar I
goto(130,0)
pendown()
sety(-20)
penup()
hideturtle()

# Función para cerrar la ventana al hacer clic
exitonclick()