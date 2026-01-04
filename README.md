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

# Creación y Gestión de Endpoints en FastAPI para CRUD de Clientes

# Actualización de Clientes: Implementación de Endpoint PATCH

# Estructuración de Aplicaciones con FastAPI y API Router
**Estructura de la aplicación**
- .
    - app
        - __init__.py
        - main.py
        - dependencies.py
        - routers
            - __init__.py
            - customers.py
            - transactions.py
            - invoices.py
    - models.py
    - db.py
    - requirements.txt    

## Creación de Routers
## Cambio en el comando
Antes se ejecutaba 
```
fastapi dev
```
Ahora se ejecuta
```
fastapi dev app/main.py
```

# Relaciones en FastAPI y SQL Model: Creación y Uso Práctico
## Cada customer puede crear muchas transactions
Relacion de uno a muchos entre `customer` y `transaction`.

# Relaciones Muchos a Muchos en Bases de Datos con SQLModel
Se agregar el modelo `plan`

# Creación y Suscripción de Planes y Clientes en FastAPI

# Consultas Avanzadas con SQL Model y Filtrado de Estados en FastAPI

# Validación de Emails Únicos en Bases de Datos con Pydantic y FastAPI
- validar formato de email
- validar que el email no exista

# Implementación de Paginación en FastAPI con SQLModel
- crear registros de transacciones
- agregar paginacion

# Implementación de Middlewares en FastAPI para Medir Tiempos de Request

# Pruebas unitarias con FastAPI y Pytest: Configuración y Ejecución
Se agregar pytest
```
pytest app\test\test_customers.py
```

# Autenticación Básica HTTP con FastAPI

# Recursos
[FastAPI Template](https://github.com/fastapi/full-stack-fastapi-template)
