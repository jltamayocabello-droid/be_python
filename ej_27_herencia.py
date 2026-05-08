class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return "El animal hace un sonido"
    
class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Guau Guau"
    
class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: Miau"
    
terry = Perro("Terry")
tom = Gato("Tome")

print(terry.hablar())
print(tom.hablar())