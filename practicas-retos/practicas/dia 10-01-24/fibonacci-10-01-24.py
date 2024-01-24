# 4. Espiral de fibonacci.

import turtle
import random

t = turtle.Turtle()
s = turtle.Screen()

# Dibujar espiral
def dibujar_espiral():
	# El range determina el tamaño de la espiral
	for x in range(1,14):
		a = fibonacci(x)
		t.circle(a, 90)

# Generar los valores de Fibonacci
def fibonacci(n):
	fib1 = 0
	fib2 = 1
	if n == 0:
		return fib1
	elif n == 1:
		return fib2
	else:
		for i in range(n-1):
			fib = fib1 + fib2
			fib1 = fib2
			fib2 = fib
	return fib

# Ejecución del programa
s.bgcolor("white")
dibujar_espiral()
s.exitonclick()



