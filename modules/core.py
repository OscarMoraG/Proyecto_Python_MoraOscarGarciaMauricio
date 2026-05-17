"""
Función
Controlar:
menús,
navegación,
flujo principal.
"""

from modules.utils import limpiar_pantalla, pausa
from modules.crud_usuarios import registrar_usuario, listar_usuarios, buscar_usuario


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

        # ===== GESTIÓN DE USUARIOS =====

        if opcion == "1":

                if usuario["rol"] != "admin":
                    print("Aceso no permitido. Solo los administradores pueden acceder a esta sección.")
                    pausa ()
                    continue

                while True:

                    limpiar_pantalla()

                    print("=== GESTIÓN DE USUARIOS ===")

                    print("1. Registrar usuario")
                    print("2. Listar usuarios")
                    print("3. Buscar usuario")
                    print("4. Volver")

                    opcion_usuario = input("Seleccione una opcion: ")

                    if opcion_usuario == "1":
                        registrar_usuario()

                    elif opcion_usuario == "2":
                        listar_usuarios()

                    elif opcion_usuario == "3":
                        buscar_usuario()
                        break

                    else:
                        print("Opción inválida")
                        pausa()
        # ===== GESTIÓN DE CONTACTOS =====
        elif opcion == "2":
                print("\nMódulo de contactos en construcción")
                pausa()

        # ===== CERRAR SESIÓN =====

        elif opcion == "3":
                print("\nCerrando sesión...")
                pausa()
                break

        # ===== SALIR =====

        elif opcion == "4":
                print("\nSaliendo del sistema...")
                exit()

        # ===== OPCIÓN INVÁLIDA =====

        else:
                print("\nOpción inválida")
                pausa()