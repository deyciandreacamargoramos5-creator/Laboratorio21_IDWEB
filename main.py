from geometria import Rectangulo, Triangulo, Circulo
figuras = [
    Rectangulo(10, 5), 
    Triangulo(3, 4, 3, 4, 5), 
    Circulo(7)
]
for f in figuras:
    print(f"Figura: {type(f).__name__}, Área: {f.area():.2f}, Perímetro: {f.perimetro():.2f}")