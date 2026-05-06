# 🚀 FastAPI Backend - API de Productos y Usuarios

---

## 📌 Descripción

API REST construida con FastAPI que permite la gestión de usuarios y productos, incluyendo autenticación con JWT, arquitectura modular por capas y conexión a PostgreSQL. El proyecto está preparado para ejecución local, Docker y despliegue en Render.

---

## 🧰 Tecnologías usadas

- FastAPI  
- PostgreSQL  
- SQLAlchemy  
- Docker & Docker Compose  
- Pydantic  
- Python-JOSE (JWT)  
- Uvicorn  

---

## 🏗 Arquitectura

El proyecto sigue una arquitectura por capas:

- routers → endpoints de la API  
- services → lógica de negocio  
- models → modelos de base de datos (SQLAlchemy)  
- schemas → validaciones (Pydantic)  
- database → conexión a PostgreSQL  
- core → configuración general  

Flujo general:

Cliente → Router → Service → Database (PostgreSQL)

---

## ⚙️ Instalación local

git clone <url-del-repositorio>  
cd nombre-del-proyecto  

Crear entorno virtual:

python -m venv venv  

Activar entorno:

Windows:  
venv\Scripts\activate  

Mac/Linux:  
source venv/bin/activate  

Instalar dependencias:

pip install -r requirements.txt  

---

## 🔐 Variables de entorno

Crear archivo .env en la raíz del proyecto:

DATABASE_URL=postgresql+psycopg2://postgres:1234@db:5432/fastapi_db  
SECRET_KEY=mi_clave_super_secreta_123  
ALGORITHM=HS256

---

## ▶️ Cómo correr el proyecto

### Local

uvicorn app.main:app --reload  

Acceso:
http://127.0.0.1:8000/docs  

---

### Docker

docker-compose up --build  

Detener:

docker-compose down -v  

Acceso:
http://localhost:8000/docs  

---

## ☁️ Deploy en Render

1. Crear servicio Web en Render  
2. Conectar repositorio de GitHub  
3. Crear base de datos PostgreSQL en Render  
4. Agregar variables de entorno  

Build:
pip install -r requirements.txt  

Start:
uvicorn app.main:app --host 0.0.0.0 --port 10000  

---

## 📡 Endpoints principales

Auth:
POST /auth/usuarios/{id}/login/ 
POST /auth/usuarios/{id}/registro/

Usuarios:
POST /usuarios/

Productos:
POST /productos  
GET /productos  
PUT /productos/{id}  
DELETE /productos/{id}  

---

## 👨‍💻 Autor

Proyecto backend con FastAPI + PostgreSQL + Docker
