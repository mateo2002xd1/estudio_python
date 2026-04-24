from pydantic import BaseModel, Field

status_error = {"status": "error", "mensaje": "No se encontro el producto"}

class producto(BaseModel):
    codigo: int
    nombre: str
    precio: float

class usuario(BaseModel):
    nombre: str = Field(min_length=1)
    edad: int = Field(gt=0)