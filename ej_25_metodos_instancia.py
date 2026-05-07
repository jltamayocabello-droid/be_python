# Metodos de Instancia

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
persona1 = Persona("Carlos", 30)
print(persona1.saludar())