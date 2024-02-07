# Ejercicio 4: Encapsulamiento y Propiedades
# Tarea: Diseña una clase `CuentaBancaria` que encapsule el atributo `saldo`, haciéndolo privado. 
# Utiliza un decorador `@property` para obtener el saldo y un método setter para depositar dinero, 
# asegurándote de que no se pueda depositar una cantidad negativa.
# Bonus: Añade una función de retiro que verifique si hay suficiente saldo antes de permitir la transacción.

class CuentaBancaria():
    def __init__(self):
        self._saldo=0.0
    
    @property
    def obtener_saldo(self):
        return self._saldo
    
    @obtener_saldo.setter
    def ingresar_dinero(self,cantidad:float):
        if cantidad < 0:
            print("Error, número negativo")
        else:
            self._saldo += cantidad
            print(f"Has ingresado {cantidad}, el saldo actual es {self._saldo}")
    
    @obtener_saldo.setter
    def retirar_dinero(self,cantidad):
        if self._saldo > 0:
            if (self._saldo - cantidad) < 0:
                print("Error, no tienes suficiente saldo. Prueba otra cantidad menor")
            else:
                self._saldo -= cantidad
                print(f"Has retirado {cantidad}, el saldo actual es {self._saldo}")
        else:
            print("Error, el saldo actual es 0. No puedes retirar dinero")

cuenta=CuentaBancaria()
cuenta._saldo=50.0
cuenta.ingresar_dinero=100.0
cuenta.retirar_dinero=50.0

