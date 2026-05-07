class Persona:
    def __init__(self, nombre, edad, activo=True):
        self.nombre = nombre
        self.edad = edad
        self.activo = activo
        print("Soy un constructor")

        persona = Persona("Juan", 32)

class CuentaBancaria:
    def __init__(self, saldo):
        if saldo < 0:
            print("No puede ser negativo")
self.saldo = saldo

cuenta = CuentaBancaria(100)