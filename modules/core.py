"""
Función
Controlar:
menús,
navegación,
flujo principal.
"""

from modules.utils import limpiar_pantalla, pausa

def menu_principal(usuario):

    while True:

        limpiar_pantalla()

        print("=== SISTEMA DE CONTACTOS ACME ===")
        print(f"Usuario: {usuario['nombres']} {usuario['apellidos']}")
        print(f"Rol: {usuario['rol']}")

        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Gestión de usuarios")
        print("2. Gestión de contactos")
        print("3. Cerrar sesión")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("Modulo de usuarios en construccion")
            pausa()

        elif opcion == '2':
            print("Modulo de contactos en construccion")
            pausa()

        elif opcion == '3':
            print("Cerrando sesión...")
            pausa()
            break

        elif opcion == '4':
            print("Saliendo del programa...")
            pausa()
            exit()

        else:
            print("Opcion invalida")
            pausa()
