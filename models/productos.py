from pydantic import BaseModel, Field

productos_db = []

class producto(BaseModel):
    codigo: int = Field(gt=0)
    nombre: str = Field(min_length=1)
    precio: float = Field(gt=0)

class usuario(BaseModel):
    nombre: str = Field(min_length=1)
    edad: int = Field(gt=0)