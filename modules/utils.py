"""
Función
Guardar funciones reutilizables como:

leer JSON,
guardar JSON,
limpiar pantalla,
pausas.
"""

import json
import os

RUTA_ARCHIVO = "data/agenda.json"

def cargar_datos():
    with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)
    return datos

def guardar_datos(datos):
    with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False )

def limpiar_pantalla():
    os.system("clear")

def pausa():
    input("\nPresione ENTER para continuar...")
