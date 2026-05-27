import json
from modules.utils import cargar_datos, pausa


def auditar_datos():

    print("=== AUDITORÍA DE DATOS ===")

    datos = cargar_datos()

    reporte = {
        "usuarios_con_errores": [],
        "contactos_con_errores": [],
        "resumen": {
            "total_usuarios": 0,
            "total_contactos": 0,
            "usuarios_con_errores": 0,
            "contactos_con_errores": 0,
            "usuarios_con_email_duplicado": 0,
            "contactos_con_id_duplicado": 0
        }
    }

    emails = []

    for usuario in datos["usuarios"]:

        errores = []

        reporte["resumen"]["total_usuarios"] += 1

        campos_obligatorios = [
            "id",
            "nombres",
            "apellidos",
            "telefono",
            "email",
            "direccion",
            "password",
            "rol"
        ]

        # VALIDAR CAMPOS OBLIGATORIOS

        for campo in campos_obligatorios:

            if campo not in usuario or usuario[campo] == "":
                errores.append(f"Falta el campo {campo}")

        # VALIDAR TELÉFONO

        if not usuario["telefono"].isdigit():
            errores.append("El campo teléfono debe contener solo dígitos")

        # VALIDAR EMAIL

        if "@" not in usuario["email"] or "." not in usuario["email"]:
            errores.append("El campo email debe tener un formato válido")

        # VALIDAR ROL

        roles_validos = ["admin", "user"]

        if usuario["rol"] not in roles_validos:
            errores.append("Rol inválido, debe ser 'admin' o 'user'")

        # VALIDAR EMAIL DUPLICADO

        if usuario["email"] in emails:

            errores.append("Email duplicado")

            reporte["resumen"]["usuarios_con_email_duplicado"] += 1

        else:
            emails.append(usuario["email"])

        # GUARDAR USUARIOS CON ERRORES

        if len(errores) > 0:

            reporte["usuarios_con_errores"].append({
                "id": usuario["id"],
                "email": usuario["email"],
                "errores": errores
            })

            reporte["resumen"]["usuarios_con_errores"] += 1

            print(usuario["email"])
            print(errores)

    # ==============================================
    # ============AUDITORÍA DE CONTACTOS============
    # ==============================================    

    ids_contactos = []

    for contacto in datos["contactos"]:
        
        errores = []

        reporte["resumen"]["total_contactos"] += 1

        campos_obligatorios = [
            "id",
            "nombres",
            "apellidos",
            "telefono",
            "email",
            "tipo_contacto"
        ]

        # VALIDAR CAMPOS OBLIGATORIOS

        for campo in campos_obligatorios:

            if campo not in contacto or contacto[campo] == "":
                errores.append(f"Falta el campo {campo}")

        # VALIDAR TELÉFONO

        if not contacto["telefono"].isdigit():
            errores.append("El teléfono debe contener solo dígitos")

        # VALIDAR EMAIL

        if "@" not in contacto["email"] or "." not in contacto["email"]:
            errores.append("El email tiene formato inválido")

        # VALIDAR TIPO DE CONTACTO

        tipos_validos = [
            "cliente",
            "proveedor",
            "aliado",
            "personal"
        ]

        if contacto["tipo_contacto"] not in tipos_validos:
            errores.append("Tipo de contacto inválido")

        # VALIDAR ID DUPLICADO

        if contacto["id"] in ids_contactos:

            errores.append("ID duplicado")

            reporte["resumen"]["contactos_con_id_duplicado"] += 1

        else:
            ids_contactos.append(contacto["id"])

        # GUARDAR CONTACTOS CON ERROR

        if len(errores) > 0:

            reporte["contactos_con_errores"].append({
                "id": contacto["id"],
                "errores": errores
            })

            reporte["resumen"]["contactos_con_errores"] += 1

            print(contacto["id"])
            print(errores)


        with open("data/reporte_auditoria_datos.json", "w") as archivo:

                json.dump(reporte, archivo, indent=4, ensure_ascii=False)

        print("Reporte de auditoría generado correctamente.")

    pausa()


