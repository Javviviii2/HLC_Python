from functions import *
juego_en_curso, jugadores,jugador_actual, tablero = iniciar_juego()

while juego_en_curso:

    if tablero_completo(tablero):
        juego_en_curso = False
        os.system("cls")
        print("Fin del juego, no hay ganador")
        break
    
    #IA first movement
    flag= True
    if flag == True:
        actualizar_tablero(tablero,5,jugadores[1][1])
        #Siguiente turno Humano
        imprimir_tablero(tablero)
        #Selección de casilla humano
        coordenada=int(input("Selecciona coordenada: "))
        if coordenada < 1 or coordenada > 9:
            print("error")
        #Actualizar tablero
        actualizar_tablero(tablero,coordenada,jugadores[0][1])
        flag=False

    #Nuevo turno
    turno = jugadores[jugador_actual]
    print("Turno de " + turno[0])

    #Si es el turno de IA que ponga la coordenada automáticamente
    if str(turno[0]) == str(jugadores[1][0]):
        coordenada= random.randint(1,9)
        #Actualizar tablero
        actualizar_tablero(tablero,coordenada,turno[1])
        progretion()
    
    #Si el jugador es humano introducir coordenadas
    elif str(turno[0]) == str(jugadores[0][0]):
        #Mostrar tablero
        imprimir_tablero(tablero)
        #Selección de casilla 
        coordenada=int(input("Selecciona coordenada: "))
        if coordenada < 1 or coordenada > 9:
            print("error")
        #Actualizar tablero
        actualizar_tablero(tablero,coordenada,turno[1])
    
    if comprobar_ganador(jugadores[jugador_actual], tablero):
        juego_en_curso = False
        imprimir_tablero(tablero)
        print("Ganador: ",jugadores[jugador_actual][0])
    
    #Cambio de jugador
    jugador_actual=turn_change(jugador_actual)