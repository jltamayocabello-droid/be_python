# Metodos de Instancia

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
persona1 = Persona("Carlos", 30)
print(persona1.saludar())

# Metodos de clase

class Usuario:
    cantidad_usuarios = 0

    def __init__(self, nombre):
        self.nombre = nombre
        Usuario.cantidad_usuarios += 1

    @classmethod
    def obtener_cantidad_usuarios(cls):
        return cls.cantidad_usuarios
    
juan = Usuario("Juan")
pedro = Usuario("Elizabeth")
print(Usuario.obtener_cantidad_usuarios())

# Metodos estáticos
class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b
    
resultado = Calculadora.sumar(200, 4)