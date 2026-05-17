
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

    print("\n=== LISTA DE USUARIOS ===")

    for usuario in datos["usuarios"]:

        print(f"""
                ID: {usuario['id']}
                Nombre: {usuario['nombres']} {usuario['apellidos']}
                Teléfono: {usuario['telefono']}
                E-mail: {usuario['email']}
                Rol: {usuario['rol']}
                -----------------------------
                """)
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