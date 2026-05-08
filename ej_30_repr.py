class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __repr__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

persona1 = Persona("Carlos", 25)
print(repr(persona1))

personas = [persona1]
print(personas)