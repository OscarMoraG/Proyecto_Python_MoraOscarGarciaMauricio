
"""
Arcihvo princial
Iniciar el programa,
mostrar login,
ejecutar el menú principal.
"""
from modules.crud_user import iniciar_sesion, buscar_email
from modules.core import menu_principal
from modules.messages import BIENVENIDA, ERROR_LOGIN

while True:

    print(BIENVENIDA)
    
    email = input("Ingrese su e-mail: ")

    usuario_encontrado = buscar_email(email)

    if not usuario_encontrado:
        print("El correo no existe")
        continue

    password = input("Ingrese su contraseña: ")

    usuario = iniciar_sesion(email, password)

    if usuario:

        print(f"Bienvenido {usuario['nombres']} {usuario['apellidos']}")

        menu_principal(usuario)

    else:
        print(ERROR_LOGIN)



