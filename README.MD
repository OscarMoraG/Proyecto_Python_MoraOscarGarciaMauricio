# Gestor de Lista de Contactos — ACME Solutions

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de gestión de contactos realizado en Python por consola para la empresa ACME Solutions.

El sistema permite administrar usuarios y contactos de manera organizada, centralizada y persistente utilizando archivos JSON como almacenamiento de datos.

El programa fue desarrollado siguiendo una arquitectura modular y aplicando conceptos básicos de programación como:

- funciones
- ciclos
- condicionales
- listas
- diccionarios
- persistencia de datos
- modularización
- CRUD
- manejo de archivos JSON

---

# Objetivo del sistema

Permitir que los empleados de la empresa puedan:

- iniciar sesión
- registrar usuarios del sistema
- administrar contactos
- consultar información
- actualizar datos
- eliminar registros
- mantener la información guardada incluso después de cerrar el programa

---

# Funcionalidades principales

## Sistema de Login

El programa inicia solicitando:

- correo corporativo
- contraseña

Solo los usuarios registrados pueden acceder al sistema.

---

# Gestión de usuarios

El sistema permite:

- Registrar usuarios
- Listar usuarios
- Buscar usuarios
- Actualizar usuarios
- Eliminar usuarios

### Restricción de seguridad

Solo los usuarios con rol `admin` pueden acceder al módulo de gestión de usuarios.

---

# Gestión de contactos

El sistema permite:

- Registrar contactos
- Listar contactos
- Buscar contactos
- Actualizar contactos
- Eliminar contactos

Los contactos pueden clasificarse por tipo:

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