#Laboratorio N° 21 - Ejercicio 06
#Autor: Andrea Camargo
#Colaboro: 
#Tiempo: 20 minutos

import math

class Figura:
    def area(self): pass
    def perimetro(self): pass

class Rectangulo(Figura):
    def __init__(self, b, h): 
        self.b, self.h = b, h
    def area(self): 
        return self.b * self.h
    def perimetro(self): 
        return 2 * (self.b + self.h)

class Triangulo(Figura):
    def __init__(self, b, h, l1, l2, l3): 
        self.b, self.h, self.l1, self.l2, self.l3 = b, h, l1, l2, l3
    def area(self): 
        return (self.b * self.h) / 2
    def perimetro(self): 
        return self.l1 + self.l2 + self.l3

class Circulo(Figura):
    def __init__(self, r): 
        self.r = r
    def area(self): 
        return math.pi * (self.r ** 2)
    def perimetro(self): 
        return 2 * math.pi * self.r