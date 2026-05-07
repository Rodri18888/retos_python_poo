"""
Crear una clase Libro con atributos y métodos para gestionar información básica

Crea una clase llamada `Libro` que represente un libro en una biblioteca. La clase debe tener los siguientes atributos:

- `titulo`: el título del libro
- `autor`: el autor del libro
- `paginas`: el número total de páginas
- `disponible`: un booleano que indica si el libro está disponible para préstamo (inicialmente `True`)

La clase debe tener los siguientes métodos:

1. Un constructor (`__init__`) que inicialice los atributos mencionados
2. Un método `prestar()` que cambie el estado de disponibilidad a `False` y devuelva un mensaje indicando que el libro ha sido prestado. Si el libro ya está prestado, debe devolver un mensaje indicando que no está disponible.
3. Un método `devolver()` que cambie el estado de disponibilidad a `True` y devuelva un mensaje indicando que el libro ha sido devuelto. Si el libro ya está disponible, debe devolver un mensaje indicando que el libro ya estaba en la biblioteca.
4. Un método `informacion()` que devuelva una cadena con toda la información del libro, incluyendo su estado de disponibilidad.
"""

#Clase libro + constructor init

class Libro:
    def __init__(self, titulo, autor, paginas):
       self.titulo = titulo
       self.autor = autor

       if paginas < 0:
           raise ValueError("El numero de paginas no puede ser negativo")
           
       self.paginas = paginas
       self.disponible = True

       #Metodo prestar()
      
    def prestar(self):
           if self.disponible:
               self.disponible = False
               return f"El libro {self.titulo} ha sido prestado con exito"
           else:
               return f"El libro {self.titulo} no se encuentra disponible"
            
       #Metodo devolver()
    def devolver(self):
           if not self.disponible:
               self.disponible = True
               return f"El libro {self.titulo} ha sido devuelto"
           else:
               return f"El libro {self.titulo} ya se encuentra en la biblioteca"
             
       #Metodo informacion()
    def informacion(self):
           print("--Informacion del libro--")
           print(f"Nombre del libro: {self.titulo}")
           print(f"Autor del libro: {self.autor}")
           print(f"Numero de paginas: {self.paginas}")
      
           if self.disponible:
               return "El libro se encuntra disponible"
           else:
               return "El libro fue prestado"
      
              
             




 

#Prueba de la clase libro

 # Crear dos objetos libro diferentes
libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 863)
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", 471)
 
 # Mostrar información inicial de los libros
print("=== Información inicial de los libros ===")
print(libro1.informacion())
print("\n")
print(libro2.informacion())
print()
 
 # Prestar los libros
print("=== Préstamo de libros ===")
print(libro1.prestar())
print(libro2.prestar())
print("\n")
 
 # Intentar prestar un libro ya prestado
print("=== Intento de préstamo de libros ya prestados ===")
print(libro1.prestar())
print("\n")
 
 # Mostrar información después del préstamo
print("=== Información después del préstamo ===")
print(libro1.informacion())
print("\n")
 
 # Devolver un libro
print("=== Devolución de libros ===")
print(libro1.devolver())
print("\n")
 
 # Intentar devolver un libro ya disponible
print("=== Intento de devolución de libros ya disponibles ===")
print(libro1.devolver())
print("\n")
 
 # Mostrar información final
print("=== Información final de los libros ===")
print(libro1.informacion())
print("\n")
print(libro2.informacion())




   