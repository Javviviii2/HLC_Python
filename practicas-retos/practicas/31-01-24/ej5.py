# Ejercicio 5: Polimorfismo y Métodos Especiales
# Tarea: Crea una clase `Vector` que represente un vector en 2D, con métodos especiales para 
# la suma (`__add__`), la resta (`__sub__`), y la representación en string (`__str__`).
# Bonus: Implementa la multiplicación de un vector por un escalar (no la multiplicación de dos vectores).

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, var_sumado):
        return Vector(self.x + var_sumado.x, self.y + var_sumado.y)

    def __sub__(self, var_restado):
        return Vector(self.x - var_restado.x, self.y - var_restado.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(5, 5)
v2 = Vector(6, 7)

print(v1 + v2)
print(v1 - v2)
print(v1)
