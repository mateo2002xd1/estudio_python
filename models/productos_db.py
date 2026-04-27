from database import Base
from sqlalchemy import Column, Integer, String, Float

class Producto(Base):
    __tablename__ = "productos"

    codigo = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float, nullable=False)

class Usuario(Base):
    __tablename__ = "usuarios"
    
    nombre = Column(String, primary_key=True, index=True)
    edad = Column(Integer, nullable=False)