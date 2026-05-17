"""
Función

CRUD de contactos.
"""
from modules.utils import cargar_datos, guardar_datos, pausa

def registrar_contacto():
    datos = cargar_datos()

    print("=== REGISTRAR CONTACTO ===")

    id_contacto = input("ID del contacto: ")

    for contacto in datos["contactos"]:

        if contacto["id"] == id_contacto:
            print("El ID ya existe")
            pausa()
            return

    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    telefono = input("Teléfono: ")
    email = input("E-mail: ")
    direccion = input("Dirección: ")
    tipo_contacto = input("Tipo de contacto: ")
    notas = input("Notas: ")

    nuevo_contacto = {
        "id": id_contacto,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "tipo_contacto": tipo_contacto,
        "notas": notas
    }

    datos["contactos"].append(nuevo_contacto)

    guardar_datos(datos)

    print("Contacto registrado correctamente")
    pausa()

def listar_contactos():

    datos = cargar_datos()

    print("\nLista de contactos")
    print("-" * 120)

    print(
        f"{'ID':<10}"
        f"{'Nombre completo':<30}"
        f"{'Telefono':<20}"
        f"{'E-mail':<35}"
        f"{'Tipo':<15}"
    )

    print("-" * 120)

    for contacto in datos["contactos"]:

        nombre_completo = (
            f"{contacto['nombres']} {contacto['apellidos']}"
        )

        print(
            f"{contacto['id']:<10}"
            f"{nombre_completo:<30}"
            f"{contacto['telefono']:<20}"
            f"{contacto['email']:<35}"
            f"{contacto['tipo_contacto']:<15}"
        )

    print("-" * 120)

    pausa()

def buscar_contacto():

    datos = cargar_datos()

    print("=== BUSCAR CONTACTO ===")

    busqueda = input(
        "Ingrese ID, nombre, apellido o tipo de contacto: "   ).lower()

    encontrados = []

    for contacto in datos["contactos"]:

        if (
            busqueda in contacto["id"].lower()
            or busqueda in contacto["nombres"].lower()
            or busqueda in contacto["apellidos"].lower()
            or busqueda in contacto["tipo_contacto"].lower()
        ):

            encontrados.append(contacto)

    if len(encontrados) == 0:
        print("No se encontraron contactos.")
        pausa()
        return

    print("\nResultados encontrados")
    print("-" * 120)

    print(
        f"{'ID':<10}"
        f"{'Nombre completo':<35}"
        f"{'Telefono':<20}"
        f"{'E-mail':<35}"
        f"{'Tipo':<15}"
    )

    print("-" * 120)

    for contacto in encontrados:

        nombre_completo = (
            f"{contacto['nombres']} {contacto['apellidos']}"
        )

        print(
            f"{contacto['id']:<10}"
            f"{nombre_completo:<35}"
            f"{contacto['telefono']:<20}"
            f"{contacto['email']:<35}"
            f"{contacto['tipo_contacto']:<15}"
        )

    print("-" * 120)

    pausa()