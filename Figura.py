import math
class Figura:
    def area(self):
        pass
    def perimetro(self):
        pass
    def mostrar_datos(self):
        print(f"Figura: {self.__class__.__name__}")
        print(f"Área: {self.area():.2f}")
        print(f"Perímetro: {self.perimetro():.2f}")
        print("-" * 30)

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(Figura):
    def __init__(self, base, lado1, lado2, altura):
        self.base = base
        self.lado1 = lado1
        self.lado2 = lado2
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2
    def perimetro(self):
        return self.base + self.lado1 + self.lado2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2
    def perimetro(self):
        return 2 * math.pi * self.radio

figuras = [
    Rectangulo(4, 6),
    Triangulo(3, 4, 5, 4),
    Circulo(5)
]
for figura in figuras:
    figura.mostrar_datos()
