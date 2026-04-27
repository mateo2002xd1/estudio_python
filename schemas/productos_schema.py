from pydantic import BaseModel, Field

class ProductoInput(BaseModel):
    codigo: int = Field(gt=0)
    nombre: str = Field(min_length=1)
    precio: float = Field(gt=0)

class UsuarioInput(BaseModel):
    nombre: str = Field(min_length=1)
    edad: int = Field(gt=0)

class ProductoResponse(BaseModel):
    codigo: int
    nombre: str
    precio: float
    
    class Config:
        from_attributes = True

class UsuarioResponse(BaseModel):
    nombre: str
    edad: int

    class Config:
        from_attributes = True