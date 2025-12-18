#Laboratorio N° 21 - Ejercicio 04
#Autor: Andrea Camargo
#Colaboro: 
#Tiempo: 20 minutos

class Libro:
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponible = True 
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"Libro '{self.titulo}' prestado con éxito"
        return f"Libro '{self.titulo}' no está disponible"

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"Libro '{self.titulo}' devuelto con éxito"
        return f"Libro '{self.titulo}' ya estaba en la biblioteca"

class LibroDigital(Libro):
    def __init__(self, titulo, autor, año, formato, tamañoMB):
        super().__init__(titulo, autor, año)
        self.formato = formato
        self.tamañoMB = tamañoMB 

    def prestar(self):
        return f"Libro digital '{self.titulo}' (Formato: {self.formato}) siempre disponible para descarga"

class Biblioteca:
    def __init__(self):
        self.libros = [] 

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        for l in self.libros:
            estado = "Disponible" if l.disponible else "Prestado"
            print(f"{l.titulo} - {l.autor} ({estado})")

    def buscar_por_autor(self, autor):
        encontrados = [l.titulo for l in self.libros if l.autor.lower() == autor.lower()]
        return encontrados if encontrados else "No se encontraron libros"

biblioteca = Biblioteca()

biblioteca.agregar_libro(Libro("La Casa de los Espíritus", "Isabel Allende", 1982))
biblioteca.agregar_libro(Libro("El Resplandor", "Stephen King", 1977))
biblioteca.agregar_libro(Libro("Crónica de una muerte anunciada", "Gabriel García Márquez", 1981))

biblioteca.agregar_libro(LibroDigital("El Imperio Final", "Brandon Sanderson", 2006, "EPUB", 4))
biblioteca.agregar_libro(LibroDigital("Palabras Radiantes", "Brandon Sanderson", 2014, "PDF", 12))

print("--- Catálogo Completo ---")
biblioteca.listar_libros()

print("--- Pruebas de Préstamo ---")
print(biblioteca.libros[1].prestar()) 
print(biblioteca.libros[1].prestar()) 

print("--- Préstamo Digital (Sanderson) ---")
for _ in range(5): 
    print(biblioteca.libros[3].prestar())

print("--- Búsqueda por Autor ---")
autor_buscado = "Brandon Sanderson"
print(f"Buscando libros de {autor_buscado}:")
print(biblioteca.buscar_por_autor(autor_buscado))