# Gestor de Lista de Contactos — ACME Solutions

## Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema de gestión de contactos realizado en Python por consola para la empresa ACME Solutions.

El sistema fue diseñado para permitir la administración de usuarios y contactos de manera organizada, centralizada y persistente mediante el uso de archivos JSON.

El proyecto fue desarrollado aplicando conceptos fundamentales de programación estructurada y modular como:

- funciones
- condicionales
- ciclos
- listas
- diccionarios
- modularización
- persistencia de datos
- manejo de archivos JSON
- CRUD
- validación de datos
- control de roles
- auditoría de información

---

# Objetivo del sistema

Permitir que los empleados de la empresa puedan:

- iniciar sesión en el sistema
- administrar usuarios
- gestionar contactos
- consultar información
- actualizar registros
- eliminar información
- almacenar datos de forma persistente
- validar la integridad de los datos almacenados

---

# Funcionalidades principales

## Sistema de Login

El sistema inicia solicitando:

- correo electrónico
- contraseña

Solo los usuarios registrados pueden acceder al sistema.

El login valida primero si el correo existe y posteriormente verifica la contraseña correspondiente.

---

# Control de roles

El sistema maneja control de acceso por roles.

## Rol admin

Los usuarios administradores pueden acceder a:

- Gestión de usuarios
- Gestión de contactos
- Auditoría de datos

## Rol user

Los usuarios estándar únicamente pueden acceder a:

- Gestión de contactos

El menú principal cambia dinámicamente según el rol autenticado.

---

# Gestión de usuarios

El módulo de usuarios permite realizar operaciones CRUD completas.

## Funcionalidades

- Registrar usuarios
- Listar usuarios
- Actualizar usuarios
- Eliminar usuarios

## Datos gestionados

Cada usuario contiene:

- id
- nombres
- apellidos
- telefono
- email
- direccion
- password
- rol

---

# Gestión de contactos

El módulo de contactos permite realizar operaciones CRUD completas.

## Funcionalidades

- Registrar contactos
- Listar contactos
- Buscar contactos
- Actualizar contactos
- Eliminar contactos

## Datos gestionados

Cada contacto contiene:

- id
- nombres
- apellidos
- telefono
- email
- tipo_contacto

## Tipos de contacto permitidos

- cliente
- proveedor
- aliado
- personal

---

# Persistencia de datos

Toda la información del sistema se almacena en archivos JSON.

## Archivo principal


## Auditoría de datos

La auditoría únicamente lee la información almacenada y no modifica el archivo original agenda.json.

Validaciones realizadas en usuarios

Durante la auditoría el sistema valida:

Campos obligatorios
id
nombres
apellidos
telefono
email
direccion
password
rol
Reglas de validación
teléfonos numéricos
formato válido de correo electrónico
roles válidos
correos electrónicos duplicados
Validaciones realizadas en contactos

Durante la auditoría el sistema valida:

Campos obligatorios
id
nombres
apellidos
telefono
email
tipo_contacto
Reglas de validación
teléfonos numéricos
formato válido de correo electrónico
tipos de contacto válidos
IDs duplicados
Reporte de auditoría

Al finalizar la auditoría el sistema genera automáticamente el archivo:

data/reporte_auditoria_datos.json

Este reporte contiene:

usuarios con errores
contactos con errores
descripción detallada de inconsistencias
resumen estadístico de auditoría
cantidad de duplicados encontrados
cantidad total de registros revisados


```plaintext
data/agenda.json