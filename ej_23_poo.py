# Clases

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"hola me llamo {self.persona} y tengo {self.edad} años")

# Objeto

persona1 = Persona("Juan", 23)
print(persona1.nombre)
print(persona1.edad)

persona1.prsentarse()

