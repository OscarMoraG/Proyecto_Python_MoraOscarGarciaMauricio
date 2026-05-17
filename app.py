
"""
Arcihvo princial
Iniciar el programa,
mostrar login,
ejecutar el menú principal.
"""
from modules.crud_usuarios import iniciar_sesion
from modules.core import menu_principal

while True:

    print("=== SISTEMA DE CONTACTOS ACME ===")

    email = input("Ingrese su e-mail: ")
    password = input("Ingrese su contraseña: ")

    usuario = iniciar_sesion(email, password)

    if usuario:
        print(f"\nBienvenido {usuario['nombres']} {usuario['apellidos']}")

        menu_principal(usuario)

    else:
        print("\nCredenciales incorrectas")




