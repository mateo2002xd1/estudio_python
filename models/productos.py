from pydantic import BaseModel, Field
from database import Base
from sqlalchemy import Column, Integer, String, Float

productos_db = []

class ProductoCreate(BaseModel):
    codigo: int = Field(gt=0)
    nombre: str = Field(min_length=1)
    precio: float = Field(gt=0)

class UsuarioCreate(BaseModel):
    nombre: str = Field(min_length=1)
    edad: int = Field(gt=0)

class Producto(Base):
    __tablename__ = "productos"

    codigo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)