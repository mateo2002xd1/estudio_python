from fastapi import FastAPI
from app.routers.productos_endpoints import router as productos_router
from app.routers.auth_endpoints import router as auth_router
from app.routers.usuarios_endpoints import router as usuarios_router
from app.database import Base, engine
from app.models.productos_db import Producto
from app.models.usuarios_db import Usuario

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(productos_router)
app.include_router(usuarios_router)
app.include_router(auth_router)