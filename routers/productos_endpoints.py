from fastapi import APIRouter
from services.productos_service import (
    post_ingresar_producto,
    get_mostrar_productos,
    get_mostrar_producto_codigo,
    put_reemplazar_producto
)
from models.productos import producto

router = APIRouter(prefix="/productos")

@router.post("/")
def post_ingresar_producto_endpoint(producto_test: producto):
        return post_ingresar_producto(producto_test)

@router.get("/")
def get_mostrar_productos_endpoint():
        return get_mostrar_productos()

@router.get("/{codigo}")
def get_mostrar_producto_codigo_endpoint(codigo: int):
    return get_mostrar_producto_codigo(codigo)

@router.put("/{codigo}")
def put_reemplazar_producto_endpoint(codigo: int, producto_body: producto):
    return put_reemplazar_producto(codigo, producto_body)