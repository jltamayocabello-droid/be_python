from abc import ABC, abstractclassmethod

class Figura(ABC):
    @abstractclassmethod
    def area(self):
        pass

    @abstractclassmethod
    def perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)
    
rect = Rectangulo(4, 5)
print(rect.area())
print(rect.perimetro())