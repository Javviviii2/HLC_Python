# Ejercicio 2: Uso de Constructores
# Tarea: Define una clase `Estudiante` con un constructor que acepte `nombre` y `edad`. Añade un método `es_mayor()` que retorne `True` si el estudiante es mayor de edad (18 años o más).
# Bonus: Incluye un atributo de lista `calificaciones` y un método que calcule el promedio de calificaciones.
import numpy as np

class Estudiante():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def es_mayor(self):
        if self.edad > 18:
            return True
        else:
            return False
    
    calificaciones=[]
    def promedio(self):
        media=np.mean(self.calificaciones)
        return media

student=Estudiante("Pedro",17)
print(student.es_mayor())
#Bonus
notas=[10,6,7,8,1,8,9]
student.calificaciones.append(notas)
print(student.promedio())