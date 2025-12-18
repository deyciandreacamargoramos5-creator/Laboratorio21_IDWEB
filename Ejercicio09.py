#Laboratorio N° 21 - Ejercicio 09
#Autor: Andrea Camargo
#Colaboro: 
#Tiempo: 20 minutos

import threading
import multiprocessing
import asyncio
import time
import random

def consulta_bd(n):
    t = random.randint(1, 5)
    time.sleep(t)
    print(f"  -> Consulta {n} terminada en {t}s")
    return t

def test_hilos():
    print("\nIniciando prueba con Hilos...")
    inicio = time.time()
    hilos = []
    for i in range(1, 4):
        h = threading.Thread(target=consulta_bd, args=(i,))
        hilos.append(h)
        h.start()
    for h in hilos:
        h.join()
    print(f"Total Hilos: {time.time() - inicio:.2f}s")

def test_procesos():
    print("\nIniciando prueba con Procesos...")
    inicio = time.time()
    procesos = []
    for i in range(1, 4):
        p = multiprocessing.Process(target=consulta_bd, args=(i,))
        procesos.append(p)
        p.start()
    for p in procesos:
        p.join()
    print(f"Total Procesos: {time.time() - inicio:.2f}s")

async def consulta_async(n):
    t = random.randint(1, 5)
    await asyncio.sleep(t)
    print(f"  -> Async {n} terminada en {t}s")

async def test_async():
    print("\nIniciando prueba con Asyncio...")
    inicio = time.time()
    await asyncio.gather(consulta_async(1), consulta_async(2), consulta_async(3))
    print(f"Total Asyncio: {time.time() - inicio:.2f}s")

if __name__ == "__main__":
    test_hilos()
    test_procesos()
    asyncio.run(test_async())