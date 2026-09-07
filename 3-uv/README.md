# 3-UV

## Comandos básicos de uv

```bash
# Crear un proyecto nuevo (genera pyproject.toml, .python-version, main.py y README.md)
uv init nombre-proyecto

# O inicializar uv dentro de una carpeta ya existente
uv init

# Agregar una dependencia (la instala y la registra en pyproject.toml + uv.lock)
uv add sqlalchemy

# Quitar una dependencia
uv remove sqlalchemy

# Sincronizar el entorno con lo declarado en pyproject.toml / uv.lock
uv sync

# Ejecutar un script dentro del entorno del proyecto (sin activarlo a mano)
uv run main.py
```

## Activar el entorno virtual

`uv` crea la carpeta `.venv` automáticamente y `uv run` la usa sin necesidad de activarla.
Si se necesita activar manualmente (por ejemplo, para que el editor o la terminal la tomen):

```bash
# Linux / macOS
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Salir del entorno
deactivate
```

## Abrir el proyecto en VS Code

Conviene abrir VS Code **desde la carpeta que contiene el entorno** (donde están `pyproject.toml` y `.venv`),
para que detecte el intérprete de `.venv` automáticamente:

```bash
cd 3-sqlalchemy
code .
```

Si no toma el intérprete solo: `Ctrl+Shift+P` → *Python: Select Interpreter* → elegir el de `./.venv/bin/python`.
