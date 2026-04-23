from fastapi import FastAPI, Query, APIRouter

app = FastAPI()

productos_lista = [
    {"codigo": 1, "nombre": "Arroz", "precio": 5000},
    {"codigo": 2, "nombre": "Leche", "precio": 4000},
    {"codigo": 3, "nombre": "Papa", "precio": 2000},
]

status_error = {"status": "error", "mensaje": "No se encontro el producto"}


def get_producto_id(id: int):
    if id < 0:
        return status_error
    for producto in productos_lista:
        if producto["codigo"] == id:
            return {"status": "ok", "data": producto}
    return status_error


def get_producto_nombre(nombre: str):
    producto_nombre = []
    for producto in productos_lista:
        if nombre.lower() in producto["nombre"].lower():
            producto_nombre.append(producto)
    if len(producto_nombre) > 0:
        return {"status": "ok", "data": producto_nombre}
    return status_error

def get_producto(id: int = None, nombre: str = None):
    if id is not None:
        return get_producto_id(id)
    if nombre is not None:
        return get_producto_nombre(nombre)
    return status_error


@app.get("/producto")
def productos(id: int = None, nombre: str = None):
    return get_producto(id, nombre)
