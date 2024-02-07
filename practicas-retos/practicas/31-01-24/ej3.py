# Ejercicio 3: Herencia
# Tarea: Crea una clase base `Animal` con un método `hacer_sonido()`. Deriva dos clases `Perro` y `Gato` de `Animal`, 
# y sobrescribe el método `hacer_sonido()` para que retorne "Guau" y "Miau", respectivamente.
# Bonus: Añade un atributo `nombre` en la clase `Animal` y demuestra cómo se puede acceder desde las clases derivadas.

class Animal():
    def __init__(self,sonido, nombre):
        self.sonido=sonido
        self.nombre=nombre
        
    def hacer_sonido(self):
        print(self.nombre + " hace " + self.sonido)

class Perro(Animal):
    def __init__(self, sonido, nombre):
        super().__init__(sonido, nombre) #super() hace refencia a su padre sin necesidad de escribir el nombre de este
class Gato(Animal):
    def __init__(self, sonido, nombre):
        super().__init__(sonido, nombre)


perro=Perro("Guau","Tintin")
perro.hacer_sonido()
gato=Gato("Miau","Misifu")
gato.hacer_sonido()
