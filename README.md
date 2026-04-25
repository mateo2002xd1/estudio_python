# estudio_python
API CRUD de productos
    -Permite:
        -Ingresar, Listar, Buscar por codigo, Actualizar y Eliminar productos

Tecnologias usadas: Python framework FastAPI

Para correcta ejecucion es necesario, Python, framework FastAPI, Ovicorn(ejecucion servidor) 
    Crear entorno virtual:
        python -m venv venv
    Activar entorno:
        Windows:
            venv\Scripts\activate
    Instalar dependencias:
        pip install fastapi uvicorn
    Ejecutar servidor:
        uvicorn main:app --reload

Endpoints
    POST /productos
    GET /productos
    GET /productos/{codigo}
    PUT /productos/{codigo}
    DELETE /productos/{codigo}