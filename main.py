from fastapi import FastAPI, Query, APIRouter
from services.productos_service import (
    producto,
    post_ingresar_producto,
    get_mostrar_productos,
    get_mostrar_producto_codigo
)

app = FastAPI()
router = APIRouter(prefix="/api")

@router.post("/producto")
def post_ingresar_producto_endpoint(producto_test: producto):
        return post_ingresar_producto(producto_test)

@router.get("/productos")
def get_mostrar_productos_endpoint():
        return get_mostrar_productos()

@router.get("/producto_db/{codigo}")
def get_mostrar_producto_codigo_endpoint(codigo: int):
    return get_mostrar_producto_codigo(codigo)

app.include_router(router)