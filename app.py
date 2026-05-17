
"""
Arcihvo princial
Iniciar el programa,
mostrar login,
ejecutar el menú principal.
"""
from modules.crud_usuarios import iniciar_sesion  

print("=== SISTEMA DE CONTACTOS ACME ===")

email= input("Ingrese su email: ")
contraseña = input("Ingrese su contraseña: ")

usuario = iniciar_sesion(email, contraseña)   

if usuario:
    print(f"\nBienvenido {usuario['nombres']} {usuario['apellidos']}")

else:
    print("\nEmail o contraseña incorrectos. Intente nuevamente.")






