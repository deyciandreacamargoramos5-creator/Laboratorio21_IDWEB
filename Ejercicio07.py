#Laboratorio N° 21 - Ejercicio 07
#Autor: Andrea Camargo
#Colaboro: 
#Tiempo: 20 minutos

import os

def copiar_texto(origen, destino):
    try:
        with open(origen, "r", encoding="utf-8") as f_org:
            with open(destino, "w", encoding="utf-8") as f_dest:
                for linea in f_org:
                    f_dest.write(linea)
        print("Texto copiado con éxito: '{origen}' -> '{destino}'")
    except FileNotFoundError:
        print(" Error: El archivo '{origen}' no existe.")
    except Exception as e:
        print(" Ocurrió un error inesperado: {e}")

def copiar_binario(origen, destino):
    try:
        with open(origen, "rb") as f_org:
            with open(destino, "wb") as f_dest:
                while True:
                    bloque = f_org.read(4096) 
                    if not bloque:
                        break
                    f_dest.write(bloque)
        print(" Archivo binario copiado con éxito: '{origen}' -> '{destino}'")
    except FileNotFoundError:
        print(" Error: El archivo binario '{origen}' no existe.")
    except Exception as e:
        print(" Ocurrió un error inesperado: {e}")

with open("archivo_prueba.txt", "w", encoding="utf-8") as f:
    f.write("Hola, este es un contenido de prueba para el Laboratorio 21.")

copiar_texto("archivo_prueba.txt", "copia_de_texto.txt")

if os.path.exists("imagen.png"):
    copiar_binario("imagen.png", "copia_de_imagen.png")
else:
    print("No se encontró 'imagen.png' para probar la copia binaria")