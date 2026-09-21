# Tarea Práctica: Sistema de Librería con SQLAlchemy

## Descripción

Implementar un sistema de librería online usando SQLAlchemy.

## Objetivos

- Crear modelos con relaciones usando SQLAlchemy
- Agregar, modificar y eliminar datos usando ORM
- Realizar consultas usando SQLAlchemy

## Parte 1: Modelos

Define los siguientes modelos con sus atributos.

**Category**
- `id, name, description`

**Author**
- `id, first_name, last_name, birth_date, nationality`

**Book**
- `id, title, isbn, publication_date, price, stock_quantity`

**Order**
- `id, quantity, order_date, customer_name`

## Parte 2: Relaciones

Una vez definidos los modelos, agrega las siguientes relaciones:

1. **Category — Book**: uno a muchos. Una categoría tiene muchos libros y cada libro pertenece a una sola categoría (`Book.category_id`).
2. **Author — Book**: muchos a muchos. Un autor puede escribir varios libros y un libro puede tener varios autores.
3. **Book — Order**: uno a muchos. Un libro puede aparecer en muchos pedidos y cada pedido corresponde a un solo libro (`Order.book_id`).

## Parte 3: Agregar Datos

Crear función que genere al menos:
- 3 categorías (Ficción, Ciencia, Historia)
- 5 autores
- 10 libros distribuidos entre categorías
- 8 pedidos

## Parte 4: Modificar Datos

### Operaciones de Actualización

Crear funciones que permitan:
- Actualizar stock de libros
- Cambiar precio de libros
- Aplicar descuentos por categoría

## Parte 5: Consultas

Crea funciones que consulten la base de datos usando SQLAlchemy, y que impriman los resultados de forma básica.

Consultas:

1. Obtener todos los libros
2. Libros más caros que $X
3. Autores ordenados alfabéticamente
4. Buscar libros por título (que contenga palabra)
5. Libros con nombre de categoría
6. Libros con autores (mostrar nombres)
7. Pedidos con información del libro


## Parte 6: Eliminar Datos

Crear funciones que permitan:
- Eliminar un pedido por su `id`
- Eliminar un libro (considerar qué pasa con sus pedidos y con la relación autor-libro)
- Eliminar una categoría (decidir qué hacer con los libros que le pertenecen)
- Quitar un autor de un libro sin eliminar ninguno de los dos