# Ejercicio 1: Introducción a las Clases
# Tarea: Crea una clase `Coche` que tenga dos atributos: `marca` y `modelo`. Incluye un método `mostrar_info()` que imprima "Marca: [marca], Modelo: [modelo]".
# Bonus: Añade un método `cambiar_modelo()` que permita modificar el atributo `modelo`.

class Coche():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
    
    def mostrar_info(self):
        print("Marca: " + self.marca)
        print("Modelo: " + self.modelo)
    
    def cambiar_modelo(self,nuevo_modelo):
        self.modelo=nuevo_modelo

coche=Coche("seat","ibiza")
coche.cambiar_modelo("toledo")
coche.mostrar_info()