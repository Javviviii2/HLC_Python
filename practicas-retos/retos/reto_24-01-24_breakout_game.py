import pygame
from pygame.locals import *

# Iniciar juego
pygame.init()

#Establecer tamaño de la pantalla de juego
screen_width = int(600)
screen_height= int(600)

screen = pygame.display.set_mode((screen_width, screen_height)) # Que aparezca la pantalla
pygame.display.set_caption('Romper Cositas') #título

# Define Colors
background_color=(234, 218, 184) 
block_color = (242, 85, 96) # rojo
raqueta_color = (69, 177, 232)

# Variables
columnas = 2
filas = 2
fin_juego=0
# letras 
fuente = pygame.font.SysFont('Comic Sans MS', 40)
texto_color = (255, 255, 0) #color letras

# variables velocidad juego
clock = pygame.time.Clock()
fps = 60
def mostrar_mensaje(mensaje, pos):
    # Asegúrate de tener una fuente definida (reemplaza 'nombre_de_la_fuente' con el nombre de la fuente que desees)
    fuente = pygame.font.SysFont('Arial', 60)
    texto_superficie = fuente.render(mensaje, True, texto_color)
    screen.blit(texto_superficie, pos)

# 1. Crear el muro de bloques
class bloques():
    # Definir dimensiones del muro de bloques
    def __init__(self):
        self.ancho = screen_width // columnas #Dividir el tamaño de la pantalla entre columnas para rellenar con bloques
        self.altura = 30 #píxeles de las dimensiones de la pantalla de juego
    
    # Crear los bloques
    def crear_bloques (self):
        self.bloques = [] #lista para guardar todos los bloques que voy a crear
        bloque_individual=[] #lista para guardar 1 bloque
        # loop para crear las filas de bloques
        for fila in range(filas):
            bloque_fila=[]
            # for para crear las columnas
            for columna in range(columnas):
                #dar posición x e y a cada bloque y crear el bloque
                bloque_x= columna * self.ancho
                bloque_y = fila * self.altura
                bloque_forma=Rect(bloque_x,bloque_y, self.ancho, self.altura) #crear forma del bloque
                # Crear lista con la info de cada bloque
                if fila < 2:
                    fuerza = 1
                elif fila < 4:
                    fuerza = 1
                elif fila < 6:
                    fuerza = 1
                bloque_individual = [bloque_forma,fuerza]
                #Añadir el bloque individual a la lista de bloque_fila
                bloque_fila.append(bloque_individual)
            # Añadir las filas a la lista donde están todos los bloques
            self.bloques.append(bloque_fila)
    
    # Dibujar los bloques
    def dibujar_bloques(self):
        for fila in self.bloques:
            for bloque in fila:
                if bloque[1] == 3:
                    block_col = block_color
                elif bloque[1] == 2:
                    block_col = block_color
                elif bloque[1] == 1:
                    block_col = block_color
                pygame.draw.rect(screen,block_col,bloque[0])
                # dar borde a los bloques
                pygame.draw.rect(screen,background_color,(bloque[0]),2)

# 2. Crear raqueta de juego
class raqueta():
    def __init__(self):
        #Variables de la raqueta
        # Tamaño
        self.altura = 20 #píxeles
        self.ancho = int(screen_width/columnas)
        # Posición 
        self.x = int((screen_width/2)) # que aparezca en medio de la pantalla
        self.y = screen_height - (self.altura * 2) # posición en la parte baja de la pantalla
        # Velocidad de movimiento raqueta
        self.velocidad_raqueta = 5
        # Forma
        self.forma_raqueta = Rect(int(self.x), int(self.y), int(self.ancho), int(self.altura))
        # Dirección raqueta
        self.direccion = 0
    
    def movimiento (self):
        #reiniciar dirección de movimiento
        self.direccion = 0
        tecla_presionada = pygame.key.get_pressed() # saber qué tecla se ha presionado en el teclado
        # Solo mover si se preciona fecha izquierda o derecha
        if tecla_presionada[K_LEFT] and self.forma_raqueta.left > 0: # self.forma_raqueta.left para comprobar que no se salga de la pantalla
            self.forma_raqueta.x -= self.velocidad_raqueta
            self.direccion = -1
        if tecla_presionada[K_RIGHT] and self.forma_raqueta.right < screen_width:
            self.forma_raqueta.x += self.velocidad_raqueta
            self.direccion = 1

    def dibujar_raqueta(self):
        pygame.draw.rect(screen,raqueta_color,self.forma_raqueta)


# 3. Crear la pelota
class juego_pelota():
    def __init__(self,x,y):
        #Crear variables de la pelota
        self.pelota_radio=10 #píxeles
        self.x = x - self.pelota_radio
        self.y = y

        self.forma_pelota = Rect(self.x, self.y, self.pelota_radio*2, self.pelota_radio * 2)
        self.velocidad_x = 4
        self.velocidad_y = -4
        self.fin_juego = 0 # control finalizar o no juego 
    
    def dibujar_pelota(self):
        pygame.draw.circle(screen,raqueta_color, (self.forma_pelota.x + self.pelota_radio,self.forma_pelota.y + self.pelota_radio), self.pelota_radio)
    
    def movimiento_pelota(self):
        # collision threshold
        collision_thresh = 5
        # start off with the assumption that the wall has been destroyed completely
        muro_destruido = 1
        contador_fila= 0
        for fila in muro.bloques:
            item_count = 0
            for item in fila:
                # check collision
                if self.forma_pelota.colliderect(item[0]):
                    # check if collision was from above
                    if abs(self.forma_pelota.bottom - item[0].top) < collision_thresh and self.velocidad_y > 0:
                        self.velocidad_y *= -1
                    # check if collision was from below
                    if abs(self.forma_pelota.top - item[0].bottom) < collision_thresh and self.velocidad_y < 0:
                        self.velocidad_y *= -1
                    # check if collision was from left
                    if abs(self.forma_pelota.right - item[0].left) < collision_thresh and self.velocidad_x > 0:
                        self.velocidad_x *= -1
                    # check if collision was from right
                    if abs(self.forma_pelota.left - item[0].right) < collision_thresh and self.velocidad_x < 0:
                        self.velocidad_x *= -1
                    # reduce the block's strength by doing damage to it
                    if muro.bloques[contador_fila][item_count][1] > 1:
                        muro.bloques[contador_fila][item_count][1] -= 1
                    else:
                        muro.bloques[contador_fila][item_count][0] = (0, 0, 0, 0)

                # check if block still exists, in whcih case the wall is not destroyed
                if muro.bloques[contador_fila][item_count][0] != (0, 0, 0, 0):
                    muro_destruido = 0
                # increase item counter
                item_count += 1
            # increase row counter
            contador_fila += 1
        # after iterating through all the blocks, check if the wall is destroyed
        if muro_destruido == 1:
            self.fin_juego = 1

        # colisión pared izquierda-derecha 
        if self.forma_pelota.left < 0 or self.forma_pelota.right > screen_width:
            self.velocidad_x *= -1
        # colisión arriba-abajo
        if self.forma_pelota.top < 0:
            self.velocidad_y *= -1
        if self.forma_pelota.bottom > screen_width: #pierdo juego si toco el suelo
            self.fin_juego = -1
        
        # colisión con raqueta
        if self.forma_pelota.colliderect(jugador_raqueta.forma_raqueta):
            #colision con parte arriba raqueta
            if abs(self.forma_pelota.bottom - jugador_raqueta.forma_raqueta.top) < collision_thresh and self.velocidad_y > 0:
                self.velocidad_y *= -1
                self.velocidad_x += jugador_raqueta.direccion
            else:
                self.velocidad_x *= -1

        # Velocidad pelota
        self.forma_pelota.x += self.velocidad_x
        self.forma_pelota.y += self.velocidad_y
        
        return self.fin_juego
        
# Crear bloques
muro = bloques()
muro.crear_bloques()
#Crear raqueta
jugador_raqueta=raqueta()
#Crear pelota
pelota = juego_pelota(jugador_raqueta.x + (jugador_raqueta.ancho // 2), jugador_raqueta.y - jugador_raqueta.altura)


# ############################################################### Poner el funcionamiento mi juego
turn_on_off=True # Flags para encendero apagar mi juego
while turn_on_off:
    clock.tick(fps)
    screen.fill(background_color)
    muro.dibujar_bloques() # dibujar el muro de bloques
    jugador_raqueta.dibujar_raqueta() # dibujar raqueta
    jugador_raqueta.movimiento() # movimiento raqueta
    pelota.dibujar_pelota() # dibujar pelota
    pelota.movimiento_pelota() #movimiento pelota
    fin_juego = pelota.movimiento_pelota()

    if fin_juego==1:
        mostrar_mensaje('Has GANADO!!!!', (100, screen_height // 2))
    elif fin_juego == -1:
        mostrar_mensaje('Has PERDIDO!!!!', (100, screen_height // 2))
    
    #comprobar si salgo o no de mi juego
    for envent in pygame.event.get(): #obtener eventos de pygame
        if envent.type ==pygame.QUIT: #comprobar si el evento es el de salir
            turn_on_off=False#Parar juego
            pygame.quit()

    pygame.display.update() #al terminar de hacer las cosas actualizar
