# Clase `CuentaBancaria` - Programacion Orientada a Objetos en Python
 
## Descripcion
 
Este programa implementa una clase `CuentaBancaria` que modela las operaciones basicas de una cuenta bancaria. Ademas de los conceptos fundamentales de POO vistos anteriormente, este ejercicio introduce el uso de **atributos privados por convencion** mediante el prefijo `_`, indicando que `_titular` y `_saldo` no deben ser accedidos directamente desde fuera de la clase.
 
### Clase `CuentaBancaria`
 
El constructor recibe el nombre del `titular` y un `saldo_inicial`, este ultimo con valor por defecto de `0`, lo que permite crear una cuenta sin saldo sin necesidad de pasar ese argumento. Al igual que en ejercicios anteriores, se incluye validacion para rechazar un saldo inicial negativo lanzando un `ValueError`.
 
### Metodos
 
- **`depositar(cantidad)`**: Verifica que la cantidad a depositar sea estrictamente positiva antes de sumarla al saldo. Retorna `True` si la operacion fue exitosa, `False` en caso contrario. Esto evita que depositos de cero o valores negativos modifiquen el saldo.
- **`retirar(cantidad)`**: Verifica que la cantidad a retirar no supere el saldo disponible antes de descontarla. Retorna `True` si el retiro fue posible, `False` si los fondos son insuficientes. Esto previene que el saldo quede en numeros negativos.
### Prueba de la clase
 
Se crea una cuenta a nombre de `"Rodrigo"` con un saldo inicial de `200`. Luego se prueban cuatro escenarios: un deposito valido, un intento de deposito con cantidad negativa, un retiro valido y un intento de retiro que supera el saldo disponible. Cada operacion imprime el valor booleano retornado por el metodo correspondiente, permitiendo verificar que las validaciones funcionan correctamente.
 
---
 
## Captura de ejecucion

![Captura](img\encapsulacion.png)