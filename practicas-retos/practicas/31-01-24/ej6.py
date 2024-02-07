# Ejercicio 6: Composición y Agregación
# Tarea: Construye una clase `Biblioteca` que contenga una lista de objetos `Libro`. 
# La `Biblioteca` debería tener métodos para añadir y mostrar los `Libro`s.
# Bonus: Implementa la eliminación de libros y asegúrate de que, al eliminar una `Biblioteca`, los objetos `Libro` no se destruya

class Biblioteca():
    def __init__(self):
        self.libros =[]
    
    # Método añadir libro
    def add_book(self,libro):
        self.libros.append(libro)
    
    # Método mostrar libros
    def show_book(self):
        for libro in self.libros:
            print(libro)
    
    # Método eliminar libro
    def eliminar_book(self, libro_eliminar):
        if libro_eliminar in self.libros:
            self.libros.remove(libro_eliminar)
    
    # No eliminar libros si elimino biblioteca
    def __del__(self):
        pass

libro1 ="Cien años de soledad"
libro2 = "El principito"
libro3 = "1984"
biblioteca=Biblioteca()

biblioteca.add_book(libro1)
biblioteca.add_book(libro2)
biblioteca.add_book(libro3)
biblioteca.show_book()
biblioteca.eliminar_book(libro1)
biblioteca.show_book()
del biblioteca