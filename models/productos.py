from pydantic import BaseModel, Field

class producto(BaseModel):
    codigo: int
    nombre: str
    precio: float

class usuario(BaseModel):
    nombre: str = Field(min_length=1)
    edad: int = Field(gt=0)