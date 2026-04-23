from fastapi import FastAPI, Query, APIRouter
from pydantic import BaseModel

class producto(BaseModel):
    codigo: int
    nombre: str
    precio: float

app = FastAPI()

productos = []

@app.post("/producto")
def post_ingresar_producto(producto_test: producto):
    for u in productos:
        if u.codigo == producto_test.codigo:
            return {"status": "error","message": "Producto repetido"}
    productos.append(producto_test)
    return {"status": "ok", "data": "Se guardo correctamente el producto"}

@app.get("/productos")
def get_mostrar_productos():
    return {"status": "ok", "data": productos}

@app.get("/producto/{codigo}")
def get_mostrar_producto_codigo(codigo: int):
    for test_producto in productos:
        if test_producto.codigo == codigo:
            return {"status": "ok", "data": test_producto}
    return {"status": "error","message": "no encontrado"}