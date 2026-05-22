from modules.utils import limpiar_pantalla, pausa

from modules.crud_user import (
    registrar_usuario,
    listar_usuarios,
    actualizar_usuario,
    eliminar_usuario
)

from modules.crud_contact import (
    registrar_contacto,
    listar_contactos,
    buscar_contacto,
    actualizar_contacto,
    eliminar_contacto
)

from modules.messages import OPCION_INVALIDA


def menu_principal(usuario):

    while True:

        limpiar_pantalla()

        print("=== SISTEMA DE CONTACTOS ACME ===")
        print(f"Usuario: {usuario['nombres']} {usuario['apellidos']}")
        print(f"Rol: {usuario['rol']}")

        print("\n--- MENÚ PRINCIPAL ---")

        # ===== MENÚ ADMIN =====

        if usuario["rol"] == "admin":

            print("1. Gestión de usuarios")
            print("2. Gestión de contactos")
            print("3. Cerrar sesión")
            print("4. Salir")

            opcion = input("\nSeleccione una opción: ")

            # ===== GESTIÓN DE USUARIOS =====

            if opcion == "1":

                while True:

                    limpiar_pantalla()

                    print("=== GESTIÓN DE USUARIOS ===")

                    print("1. Registrar usuario")
                    print("2. Listar usuarios")
                    print("3. Actualizar usuario")
                    print("4. Eliminar usuario")
                    print("5. Volver")

                    opcion_usuario = input("\nSeleccione una opción: ")

                    if opcion_usuario == "1":
                        registrar_usuario()

                    elif opcion_usuario == "2":
                        listar_usuarios()

                    elif opcion_usuario == "3":
                        actualizar_usuario()

                    elif opcion_usuario == "4":
                        eliminar_usuario()

                    elif opcion_usuario == "5":
                        break

                    else:
                        print(OPCION_INVALIDA)
                        pausa()

            # ===== GESTIÓN DE CONTACTOS =====

            elif opcion == "2":

                while True:

                    limpiar_pantalla()

                    print("=== GESTIÓN DE CONTACTOS ===")

                    print("1. Registrar contacto")
                    print("2. Listar contactos")
                    print("3. Buscar contacto")
                    print("4. Actualizar contacto")
                    print("5. Eliminar contacto")
                    print("6. Volver")

                    opcion_contacto = input("\nSeleccione una opción: ")

                    if opcion_contacto == "1":
                        registrar_contacto()

                    elif opcion_contacto == "2":
                        listar_contactos()

                    elif opcion_contacto == "3":
                        buscar_contacto()

                    elif opcion_contacto == "4":
                        actualizar_contacto()

                    elif opcion_contacto == "5":
                        eliminar_contacto()

                    elif opcion_contacto == "6":
                        break

                    else:
                        print(OPCION_INVALIDA)
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

            else:
                print(OPCION_INVALIDA)
                pausa()

        # ===== MENÚ USUARIO NORMAL =====

        else:

            print("1. Gestión de contactos")
            print("2. Cerrar sesión")
            print("3. Salir")

            opcion = input("\nSeleccione una opción: ")

            # ===== GESTIÓN DE CONTACTOS =====

            if opcion == "1":

                while True:

                    limpiar_pantalla()

                    print("=== GESTIÓN DE CONTACTOS ===")

                    print("1. Registrar contacto")
                    print("2. Listar contactos")
                    print("3. Buscar contacto")
                    print("4. Actualizar contacto")
                    print("5. Eliminar contacto")
                    print("6. Volver")

                    opcion_contacto = input("\nSeleccione una opción: ")

                    if opcion_contacto == "1":
                        registrar_contacto()

                    elif opcion_contacto == "2":
                        listar_contactos()

                    elif opcion_contacto == "3":
                        buscar_contacto()

                    elif opcion_contacto == "4":
                        actualizar_contacto()

                    elif opcion_contacto == "5":
                        eliminar_contacto()

                    elif opcion_contacto == "6":
                        break

                    else:
                        print(OPCION_INVALIDA)
                        pausa()

            # ===== CERRAR SESIÓN =====

            elif opcion == "2":
                print("\nCerrando sesión...")
                pausa()
                break

            # ===== SALIR =====

            elif opcion == "3":
                print("\nSaliendo del sistema...")
                exit()

            else:
                print(OPCION_INVALIDA)
                pausa()