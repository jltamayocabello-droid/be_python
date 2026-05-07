class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def obtener_saldo(self):
        return self.__saldo  # Acceso al atributo privado
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Deposito exitoso, nuevo saldo: {self.__saldo}"
        else:
            return "Cantidad invalida"
        
    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return f"Retiro exitoso, nuevo saldo: {self.__saldo}"
        else:
            return "Saldo insuficiente o cantidad invalida"
        
cuenta1 = CuentaBancaria("Alberto Rozas", 2000)
print(cuenta1.obtener_saldo)
print(cuenta1.depositar(50000))
print(cuenta1.retirar(3000))