# Gestor de Lista de Contactos — ACME Solutions

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de gestión de contactos realizado en Python por consola para la empresa ACME Solutions.

El sistema permite administrar usuarios y contactos de manera organizada, centralizada y persistente utilizando archivos JSON como almacenamiento de datos.

El programa fue desarrollado aplicando conceptos fundamentales de programación como:

- funciones
- ciclos
- condicionales
- listas
- diccionarios
- modularización
- persistencia de datos
- CRUD
- manejo de archivos JSON

---

# Objetivo del sistema

Permitir que los empleados de la empresa puedan:

- iniciar sesión
- administrar usuarios
- gestionar contactos
- consultar información
- actualizar registros
- eliminar información
- mantener persistencia de datos

---

# Funcionalidades principales

## Sistema de Login

El sistema inicia solicitando:

- correo corporativo
- contraseña

Solo los usuarios registrados pueden acceder al sistema.

---

# Gestión de usuarios

El sistema permite:

- Registrar usuarios
- Listar usuarios
- Actualizar usuarios
- Eliminar usuarios

### Control de roles

Solo los usuarios con rol `admin` pueden visualizar y acceder al módulo de gestión de usuarios.

Los usuarios con otros roles únicamente pueden acceder al módulo de contactos.

---

# Gestión de contactos

El sistema permite:

- Registrar contactos
- Listar contactos
- Buscar contactos
- Actualizar contactos
- Eliminar contactos

Los contactos pueden clasificarse por categorías como:

- cliente
- proveedor
- aliado
- personal
- entre otros

---

# Persistencia de datos

Toda la información del sistema se almacena en un archivo JSON ubicado en:

```plaintext
data/agenda.json