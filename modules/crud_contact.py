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

    print("Lista de contactos")
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

    print("Resultados encontrados")
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

def actualizar_contacto():

    datos = cargar_datos()

    print("=== ACTUALIZAR CONTACTO ===")

    id_contacto = input("Ingrese el ID del contacto: ")

    for contacto in datos["contactos"]:

        if contacto["id"] == id_contacto:

            print("Contacto encontrado")

            nuevo_nombre = input(
                f"Nombres ({contacto['nombres']}): "
            )
            if nuevo_nombre != "":
                contacto["nombres"] = nuevo_nombre

            nuevo_apellido = input(
                f"Apellidos ({contacto['apellidos']}): "
            )
            if nuevo_apellido != "":
                contacto["apellidos"] = nuevo_apellido

            nuevo_telefono = input(
                f"Teléfono ({contacto['telefono']}): "
            )
            if nuevo_telefono != "":
                contacto["telefono"] = nuevo_telefono

            nuevo_email = input(
                f"E-mail ({contacto['email']}): "
            )
            if nuevo_email != "":
                contacto["email"] = nuevo_email

            nueva_direccion = input(
                f"Dirección ({contacto['direccion']}): "
            )
            if nueva_direccion != "":
                contacto["direccion"] = nueva_direccion

            nuevo_tipo = input(
                f"Tipo de contacto ({contacto['tipo_contacto']}): "
            )
            if nuevo_tipo != "":
                contacto["tipo_contacto"] = nuevo_tipo

            nuevas_notas = input(
                f"Notas ({contacto['notas']}): "
            )
            if nuevas_notas != "":
                contacto["notas"] = nuevas_notas

            guardar_datos(datos)

            print("Contacto actualizado correctamente")
            pausa()
            return

    print("Contacto no encontrado")
    pausa()

def eliminar_contacto():

    datos = cargar_datos()

    print("=== ELIMINAR CONTACTO ===")

    id_contacto = input("Ingrese el ID del contacto a eliminar: ")

    contacto_encontrado = None

    for contacto in datos["contactos"]:

        if contacto["id"] == id_contacto:
            contacto_encontrado = contacto
            break

    if contacto_encontrado:

        print(f"""
                Contacto encontrado:

                ID: {contacto_encontrado['id']}
                Nombre: {contacto_encontrado['nombres']} {contacto_encontrado['apellidos']}
                E-mail: {contacto_encontrado['email']}
                Tipo: {contacto_encontrado['tipo_contacto']}
                """)

        confirmacion = input("¿Está seguro de eliminar este contacto? (s/n): "      ).lower()

        if confirmacion == "s":

            datos["contactos"].remove(contacto_encontrado)

            guardar_datos(datos)

            print("Contacto eliminado correctamente")

        else:
            print("Eliminación cancelada")

    else:
        print("Contacto no encontrado")

    pausa()
