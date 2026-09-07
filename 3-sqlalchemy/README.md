# Actividad Práctica SQLAlchemy: Registro de Estudiantes

## Objetivo
Crear un sistema básico de registro de estudiantes utilizando SQLAlchemy para practicar la definición de modelos, operaciones CRUD y consultas básicas.

## Actividades

### Definición del Modelo
Define un modelo `Estudiante` con los siguientes campos:
- `id`: clave primaria autoincremental
- `rut`: texto único de máximo 12 caracteres, obligatorio  
- `nombre`: texto de máximo 50 caracteres, obligatorio
- `apellido`: texto de máximo 50 caracteres, obligatorio
- `carrera`: texto de máximo 100 caracteres, obligatorio
- `año_ingreso`: entero, obligatorio
- `activo`: booleano, por defecto True
- `fecha_registro`: datetime con valor por defecto del momento actual

### Inserción de datos
Agregar estos 8 estudiantes:
1. Juan Pérez (12345678-9, Ingeniería Civil, 2024)
2. María González (98765432-1, Medicina, 2024) 
3. Carlos Rojas (11223344-5, Psicología, 2023)
4. Ana Silva (55667788-9, Derecho, 2024)
5. Luis Torres (99887766-3, Arquitectura, 2023)
6. Carmen López (44556677-8, Ingeniería Civil, 2022)
7. Pedro Martín (33445566-7, Medicina, 2023)
8. Laura Díaz (77889900-1, Psicología, 2024)

### Consultas
Implementa las siguientes consultas:
1. **Todos los estudiantes** ordenados por apellido
2. **Estudiantes de 2024** solamente
3. **Estudiante específico** por RUT (buscar "12345678-9")
4. **Contar estudiantes** por año de ingreso
5. **Estudiantes activos** de Ingeniería Civil
6. **Búsqueda por texto**: Estudiantes cuyo nombre O apellido contenga "ar" (usar `like` y `or_`)
7. **Múltiples filtros**: Estudiantes de Medicina o Psicología que hayan ingresado en 2023 o 2024 (usar `in_` para ambos campos)
8. **Rango de años**: Estudiantes que ingresaron entre 2022 y 2023 (inclusive) y están activos, ordenados por carrera y luego por año de ingreso descendente

### Modificaciones
1. Cambiar la carrera de Luis Torres a "Ingeniería en Construcción"
2. Desactivar (activo=False) a María González
3. Actualizar el año de ingreso de Carlos Rojas a 2024

### Eliminación
Eliminar al estudiante con RUT "55667788-9"

### Verificación Final
Ejecuta una consulta final que muestre todos los estudiantes activos con sus datos principales (nombre completo, carrera, año), ordenados por año de ingreso y luego por apellido.

