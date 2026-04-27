from fastapi import FastAPI
from routers.productos_endpoints import router as productos_router
from routers.usuarios_endpoints import router as usuarios_router
from database import Base, engine

app = FastAPI()

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

app.include_router(productos_router)
app.include_router(usuarios_router)