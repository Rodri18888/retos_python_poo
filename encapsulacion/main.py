"""
Crea una clase `CuentaBancaria` que implemente el concepto de encapsulación. La clase debe tener los siguientes atributos privados: `_titular` (string) y `_saldo` (float). Implementa propiedades para acceder y modificar estos atributos de forma controlada:

1. La propiedad `titular` debe permitir obtener el valor pero no modificarlo (solo lectura).
2. La propiedad `saldo` debe permitir obtener el valor y modificarlo, pero con la restricción de que no se pueda establecer un saldo negativo (debe lanzar un ValueError con el mensaje "El saldo no puede ser negativo").
3. Añade un método `depositar(cantidad)` que incremente el saldo solo si la cantidad es positiva, devolviendo True si la operación fue exitosa o False en caso contrario.
4. Añade un método `retirar(cantidad)` que disminuya el saldo solo si hay suficiente dinero, devolviendo True si la operación fue exitosa o False en caso contrario.

La clase debe inicializarse con un titular y un saldo inicial (que por defecto será 0).
"""

#Clase y metodos
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self._titular = titular

        if saldo_inicial < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        self._saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        if cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False    


#Prueba de la clase CuentaBancaria
miCuenta = CuentaBancaria("Rodrigo", 200)


# Metodo depositar
print(miCuenta.depositar(100))


# Metodo depositar(cantidad negativa)
print(miCuenta.depositar(-100))


# Metodo retirar
print(miCuenta.retirar(50))


# Metodo retirar (retiro mayor al saldo)
print(miCuenta.retirar(509000))

