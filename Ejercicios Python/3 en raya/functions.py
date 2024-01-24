import os
import random

#Función que incializa los valores del juego
def iniciar_juego():
    juego_en_curso= True
    jugadores = [
                ["Jugador Humano","O"], 
                ["Jugador IA","X"]
                ]
    jugador_actual = random.randint(0, 1)
    tablero =  [[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]
               ]
    return juego_en_curso, jugadores, jugador_actual, tablero

def turn_change(jugador_actual):
    if jugador_actual == 0:
        jugador_actual = 1
    else:
        jugador_actual = 0
    return jugador_actual

def imprimir_tablero(tablero):
    for fila in tablero:
        print("|".join(map(str, fila)))
        print("-----")

def actualizar_tablero(tablero_actual, coordenada, figura):
    for fila in range(3):
        for columna in range(3):
            if tablero_actual[fila][columna] == coordenada:
                #Comprobar que la casilla está vacía antes de colocar el símbolo
                if tablero_actual[fila][columna] != 'O' and tablero_actual[fila][columna] != 'X':
                    tablero_actual[fila][columna] = figura
                    return tablero_actual
                else:
                    return print("Movement not allowed")

# Dot waiting progretion
def progretion():
    import time, sys

    for i in range(3):
        time.sleep(.3)
        sys.stdout.write('.')
        sys.stdout.flush()
    clean_screen()

# Clean screen
def clean_screen():
    import os
    os.system('cls' if os.name=='nt' else 'clear')

#Comprobar ganador
def comprobar_ganador(jugador, tablero_actual):
    #Comprobar por filas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[i][x] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador

    #Comprobar por columnas
    for i in range(3):
        ganador = True
        for x in range(3):
            if tablero_actual[x][i] != jugador[1]:
                ganador = False
                break
        if ganador:
            return ganador

    #Comprobar por diagonales
    ganador = True
    for i in range(3):
        if tablero_actual[i][i] != jugador[1]:
            ganador = False
            break
    if ganador:
        return ganador

    ganador = True
    for i in range(3):
        if tablero_actual[i][3 - 1 - i] != jugador[1]:
            ganador = False
            break
    if ganador:
        return ganador
    
    return False

#Comprobar si tablero completo
def tablero_completo(tablero_actual):
    for linea in tablero_actual:
        for celda in linea:
            y=[]
            for x in range(1,10):
                y.append(x)
            if celda in y:
                return False
    return True