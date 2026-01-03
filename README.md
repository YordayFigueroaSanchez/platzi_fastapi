# platzi_fastapi
Curso de FastAPI de platzi

# Entorno virtual con uv
## Instalar uv
[installation-methods](https://docs.astral.sh/uv/getting-started/installation/#installation-methods)
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
## Verificar instalación
```:bash
uv --version
```
## Inicializar proyecto
```:bash
uv init
```
## Crear entorno virtual
```:bash
uv venv
```
## Activar entorno virtual
```:bash
.venv\Scripts\Activate
```
## Desactivar entorno virtual
```:bash
deactivate
```
## Respaldo de dependencias
```:bash
uv lock
```

# Creación de APIs con FastAPI: Framework Rápido y Versátil
[FastAPI](https://fastapi.tiangolo.com/)
[Pydantic](https://docs.pydantic.dev/latest/)
[Starlette](https://starlette.dev/)

# Creación de Entornos Virtuales y Configuración de FastAPI
con `pip` se ejecuta
```
pip install fastapi[standard]
```
como seria con `uv`?
```bash
uv pip install "fastapi[standard]"
uv add "fastapi[standard]"
```

## Ejecutar FastAPI
```bash
fastapi dev
```

## Agregar tzdata
```bash
uv add tzdata
```

# Validación de datos con Pydantic en FastAPI: Creación de endpoints

# Modelado de Datos y Conexión de Modelos en FastAPI

# Validación de Datos y Modelos en Endpoints de FastAPI

# Conexión de FastAPI con SQLite usando SQLModel
[SQLModel](https://sqlmodel.tiangolo.com/)
## Agregar SQLModel
```bash
uv add sqlmodel
```

# Integración de SQLModel en FastAPI para Manejo de Bases de Datos