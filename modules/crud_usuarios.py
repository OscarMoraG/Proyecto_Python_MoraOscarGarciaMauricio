
from modules.utils import cargar_datos, guardar_datos, pausa


def iniciar_sesion(email, password):

    datos = cargar_datos()     #leer datos del JSON

    for usuario in datos["usuarios"]:   #Recorrer la lista de usuarios

        if usuario["email"] == email and usuario["password"] == password:      #valida si el email y password coinciden con los datos del JSON
            return usuario

    return None

def registrar_usuario():

    datos = cargar_datos()

    print("=== Registro de Usuario ===")

    id_usuario = input("Identificacion: ")

    for usuario in datos ["usuarios"]:
        if usuario["id"] == id_usuario:
            print("El ID ya existe. Por favor, elige otro.")
            pausa()
            return
        
    email = input("E-mail coorporativo: ")

    for usuario in datos["usuarios"]:
        if usuario["email"] == email:
            print("El e-mail ya esta registrado. ")
            pausa()
            return
        
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    rol = input("Rol: ")
    password = input("Contraseña: ")
            
    nuevo_usuario = {
        "id": id_usuario,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "password": password,
        "rol": rol
    } 

    datos["usuarios"].append(nuevo_usuario)

    guardar_datos(datos)

    print("Usuario registrado con éxito.")
    pausa()

def listar_usuarios():

    datos = cargar_datos()

    print("Lista de usuarios")
    print("-" * 120)

    print(
        f"{'ID':<10}"
        f"{'Nombre completo':<30}"
        f"{'Telefono':<20}"
        f"{'E-mail':<35}"
        f"{'Rol':<10}"
    )

    print("-" * 120)

    for usuario in datos["usuarios"]:

        nombre_completo = (
            f"{usuario['nombres']} {usuario['apellidos']}"
        )

        print(
            f"{usuario['id']:<10}"
            f"{nombre_completo:<30}"
            f"{usuario['telefono']:<20}"
            f"{usuario['email']:<35}"
            f"{usuario['rol']:<10}"
        )

    print("-" * 120)

    pausa()

def buscar_usuario():

    datos = cargar_datos()

    print("=== BUSCAR USUARIO ===")

    busqueda = input("Ingrese ID, nombre o apellido: ").lower()

    encontrado = False

    for usuario in datos["usuarios"]:

        if (
            busqueda in usuario["id"].lower()
            or busqueda in usuario["nombres"].lower()
            or busqueda in usuario["apellidos"].lower()
        ):

            print(f"""
                    ID: {usuario['id']}
                    Nombre: {usuario['nombres']} {usuario['apellidos']}
                    Teléfono: {usuario['telefono']}
                    E-mail: {usuario['email']}
                    Rol: {usuario['rol']}
                    -----------------------------
                    """)

            encontrado = True

    if not encontrado:
        print("No se encontraron usuarios con los datos ingresados. ")


    pausa()

def actualizar_usuario():

    datos = cargar_datos()

    print("=== ACTUALIZAR USUARIO ===")

    id_usuario = input("Ingrese el ID del usuario a actualizar: ")

    for usuario in datos["usuarios"]:

        if usuario["id"] == id_usuario:

            print(" Usuario Encontrado. ")

            nuevo_nombre = input(f"Nombres ({usuario['nombres']}): ")
            if nuevo_nombre != "":
                usuario["nombres"] = nuevo_nombre

            nuevo_apellido = input(f"Apellidos ({usuario['apellidos']}): ")
            if nuevo_apellido != "":
                usuario["apellidos"] = nuevo_apellido

            nuevo_telefono = input(f"Teléfono ({usuario['telefono']}): ")
            if nuevo_telefono != "":
                usuario["telefono"] = nuevo_telefono

            nuevo_email = input(f"E-mail ({usuario['email']}): ")
            if nuevo_email != "":
                usuario["email"] = nuevo_email

            nueva_direccion = input(f"Dirección ({usuario['direccion']}): ")
            if nueva_direccion != "":
                usuario["direccion"] = nueva_direccion

            nuevo_rol = input(f"Rol ({usuario['rol']}): ")
            if nuevo_rol != "":
                usuario["rol"] = nuevo_rol

            nuevo_password = input("Nueva contraseña: ")
            if nuevo_password != "":
                usuario["password"] = nuevo_password

            guardar_datos(datos)

            print(" Usuario actualizado con éxito. ")
            pausa()
            return
    print(" No se encontró un usuario con el ID ingresado. ")
    pausa()

def eliminar_usuario():

    datos = cargar_datos()

    print("=== ELIMINAR USUARIO ===")

    id_usuario = input("Ingrese el ID del usuario a eliminar: ")

    usuario_encontrado = None

    #RECORRER USUARIOS
    
    for usuario in datos["usuarios"]:

        if usuario["id"] == id_usuario:
            usuario_encontrado = usuario
            break

    # VALIDAR SI EXISTE EL USUARIO

    if usuario_encontrado:
        
        print(f"""
                Usuario encontrado:

                ID: {usuario_encontrado['id']}
                Nombre: {usuario_encontrado['nombres']} {usuario_encontrado['apellidos']}
                E-mail: {usuario_encontrado['email']}
                Rol: {usuario_encontrado['rol']}
                """)
        
        confirmacion = input("¿Está seguro que desea eliminar este usuario? (s/n): ").lower()

        if confirmacion == "s":

            datos["usuarios"].remove(usuario_encontrado)

            guardar_datos(datos)

            print("Usuario eliminado con éxito.")
        else:
            print("Eliminación cancelada.")
    else:
        print("Usuario no encontrado.")        
        
        pausa()
