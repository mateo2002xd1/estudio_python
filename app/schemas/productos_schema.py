from pydantic import BaseModel, Field

class ProductoFiltro(BaseModel):
    codigo: int = Field(gt=0)

class ProductoInput(BaseModel):
    codigo: int = Field(gt=0)
    nombre: str = Field(min_length=1)
    precio: float = Field(gt=0)

class ProductoResponse(BaseModel):
    codigo: int
    nombre: str
    precio: float
    
    class Config:
        from_attributes = True