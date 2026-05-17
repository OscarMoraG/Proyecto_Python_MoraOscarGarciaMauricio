"""
Función

Contendrá el CRUD de usuarios:

Crear
Leer
Actualizar
Eliminar
"""

from modules.utils import cargar_datos   #desde utils llama cargar_datos para leer el JSON


def iniciar_sesion(email, password):

    datos = cargar_datos()     #leer datos del JSON

    for usuario in datos["usuarios"]:   #Recorrer la lista de usuarios

        if usuario["email"] == email and usuario["password"] == password:      #valida si el email y password coinciden con los datos del JSON
            return usuario

    return None