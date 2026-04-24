from fastapi import FastAPI
from routers.productos_endpoints import router as productos_router
from routers.usuarios_endpoints import router as usuarios_router

app = FastAPI()

app.include_router(productos_router)
app.include_router(usuarios_router)