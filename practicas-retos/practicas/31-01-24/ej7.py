# Ejercicio 7: Proyecto Integrador
# Tarea: Desarrolla un pequeño sistema para una tienda que incluya clases para `Producto`, `Inventario`, `Carrito` y `Cliente`. 
# Implementa funcionalidades básicas como añadir/quitar productos al inventario, añadir productos al carrito, y realizar una compra.
# Bonus: Añade un sistema de descuentos, donde ciertos productos puedan tener un descuento y este se aplique al precio final en el carrito.

class Producto:
  def __init__(self, nombre, precio, inventario):
    self.nombre = nombre
    self.precio = precio
    self.inventario = inventario

  def __repr__(self):
    return f"Producto: {self.nombre}, Precio: {self.precio}, inventario: {self.inventario}"

class Inventario:
  def __init__(self):
    self.productos = []

  def add_producto(self, producto):
    # sumar si ya existe en el inventario
    if producto.nombre in self.productos:
      self.productos[producto.nombre].inventario += producto.inventario
    else:
      self.productos[producto.nombre] = producto

  def remove_producto(self, nombre, cantidad):
    if nombre in self.productos:
        self.productos[nombre].inventario -= cantidad
    else:
      print("No está en el inventario.")

  def mostrar_productos(self):
    for producto in self.productos.values():
      print(producto)

class Carrito:
  def __init__(self):
    self.productos = {}

  def add_producto(self, producto, cantidad):
    if producto.nombre in self.productos:
      self.productos[producto.nombre].cantidad += cantidad
    else:
      print("error")

  def remove_producto(self, nombre, cantidad):
    if nombre in self.productos:
        self.productos[nombre].cantidad -= cantidad
    else:
      print("error")

  def mostrar_productos(self):
    for producto in self.productos.values():
      print(f"{producto.nombre} - Cantidad: {producto.cantidad}")

  def calcular_total(self):
    total = 0
    for producto in self.productos.values():
      total += producto.precio * producto.cantidad
    return total

class Cliente:
  def __init__(self, nombre):
    self.nombre = nombre

  def __repr__(self):
    return f"Cliente: {self.nombre}"

# Crear productos
producto1 = Producto("Camiseta", 20, 10)
# Crear inventario
inventario = Inventario()
# Crear carrito
carrito = Carrito()
# Crear cliente
cliente = Cliente("Juan")

# Agregar productos al inventario
inventario.add_producto(producto1)

# Agregar productos al carrito
carrito.add_producto(producto1, 2)

# Mostrar productos en el carrito
carrito.mostrar_productos()

# Calcular total
total = carrito.calcular_total()
print(total)

# eliminar
inventario.remove_producto(producto1.nombre, 2)

# Mostrar inventario
inventario.mostrar_productos()
