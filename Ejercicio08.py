#Laboratorio N° 21 - Ejercicio 08
#Autor: Andrea Camargo
#Colaboro: 
#Tiempo: 20 minutos

import json

equipos = [
    {"Nombre": "Real Madrid", "país": "España", "nivelAtaque": 95, "nivelDefensa": 90},
    {"Nombre": "Manchester City", "país": "Inglaterra", "nivelAtaque": 98, "nivelDefensa": 88},
    {"Nombre": "Bayern Munich", "país": "Alemania", "nivelAtaque": 92, "nivelDefensa": 85}
]

cadena_json = json.dumps(equipos, indent=4, ensure_ascii=False)

print("--- Cadena JSON de Equipos ---")
print(cadena_json)