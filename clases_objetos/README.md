# Clase `Libro` - Programacion Orientada a Objetos en Python
 
## Descripcion
 
Este programa implementa una clase `Libro` que modela el comportamiento basico de un libro dentro de un sistema de biblioteca. El objetivo es demostrar los fundamentos de la Programacion Orientada a Objetos (POO): definicion de clases, uso del constructor `__init__`, atributos de instancia, metodos de comportamiento y validacion de datos.
 
### Clase `Libro`
 
La clase cuenta con un constructor que recibe tres parametros obligatorios: `titulo`, `autor` y `paginas`. Ademas de almacenarlos como atributos de instancia, el constructor incluye una validacion que lanza una excepcion `ValueError` si el numero de paginas es negativo, evitando la creacion de objetos con datos invalidos. Tambien inicializa automaticamente el atributo `disponible` en `True`, representando que el libro se encuentra en la biblioteca al momento de su creacion.
 
### Metodos
 
La clase define tres metodos de comportamiento:
 
- **`prestar()`**: Verifica si el libro esta disponible. Si lo esta, cambia `disponible` a `False` y retorna un mensaje de exito. Si ya fue prestado, informa que no esta disponible. Esto previene que un mismo libro sea prestado dos veces al mismo tiempo.
- **`devolver()`**: Realiza la logica inversa a `prestar()`. Solo permite devolver un libro que efectivamente fue prestado, cambiando `disponible` de vuelta a `True`. Si el libro ya estaba en la biblioteca, lo indica.
- **`informacion()`**: Imprime los datos del libro (titulo, autor, paginas) y retorna un mensaje indicando su estado de disponibilidad actual.
### Prueba de la clase
 
El programa crea dos objetos `Libro` distintos (`libro1` y `libro2`) y ejecuta una serie de operaciones sobre ellos para verificar el comportamiento de cada metodo: muestra la informacion inicial, realiza prestamos, intenta prestar libros ya prestados, devuelve uno y verifica el estado final. Cada bloque de operaciones esta delimitado por mensajes de seccion para facilitar la lectura de la salida en consola.
 
---
 
## Captura de ejecucion
 
