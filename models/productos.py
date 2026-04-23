from pydantic import BaseModel

status_error = {"status": "error", "mensaje": "No se encontro el producto"}

class producto(BaseModel):
    codigo: int
    nombre: str
    precio: float