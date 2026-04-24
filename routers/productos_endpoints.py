from fastapi import APIRouter
from services.productos_service import (
<<<<<<< HEAD
    producto,
    post_ingresar_producto,
    get_mostrar_productos,
    get_mostrar_producto_codigo
)

router = APIRouter(prefix="/productos")

@router.post("/ingresar")
def post_ingresar_producto_endpoint(producto_test: producto):
        return post_ingresar_producto(producto_test)

@router.get("/mostrar_all")
def get_mostrar_productos_endpoint():
        return get_mostrar_productos()

@router.get("/mostrar_code/{codigo}")
def get_mostrar_producto_codigo_endpoint(codigo: int):
    return get_mostrar_producto_codigo(codigo)
=======
    ingresar_producto,
    mostrar_productos,
    mostrar_producto_codigo,
    reemplazar_producto,
    eliminar_producto
)
from models.productos import producto

router = APIRouter(prefix="/productos")

@router.post("/")
def ingresar_producto_endpoint(producto_test: producto):
        return ingresar_producto(producto_test)

@router.get("/")
def mostrar_productos_endpoint():
        return mostrar_productos()

@router.get("/{codigo}")
def mostrar_producto_codigo_endpoint(codigo: int):
    return mostrar_producto_codigo(codigo)

@router.put("/{codigo}")
def reemplazar_producto_endpoint(codigo: int, producto_body: producto):
    return reemplazar_producto(codigo, producto_body)

@router.delete("/{codigo}")
def eliminar_producto_endpoint(codigo: int):
      return eliminar_producto(codigo)
>>>>>>> c56ca4bb137baba9beda49c920459f7606142854
