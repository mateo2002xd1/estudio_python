from fastapi import APIRouter
from services.productos_service import (
    ingresar_producto,
    mostrar_productos,
    mostrar_producto_codigo,
    reemplazar_producto,
    eliminar_producto
)
from models.productos import ProductoCreate

router = APIRouter(prefix="/productos")

@router.post("/")
def ingresar_producto_endpoint(producto_test: ProductoCreate):
        return ingresar_producto(producto_test)

@router.get("/")
def mostrar_productos_endpoint():
        return mostrar_productos()

@router.get("/{codigo}")
def mostrar_producto_codigo_endpoint(codigo: int):
    return mostrar_producto_codigo(codigo)

@router.put("/{codigo}")
def reemplazar_producto_endpoint(codigo: int, producto_body: ProductoCreate):
    return reemplazar_producto(codigo, producto_body)

@router.delete("/{codigo}")
def eliminar_producto_endpoint(codigo: int):
      return eliminar_producto(codigo)