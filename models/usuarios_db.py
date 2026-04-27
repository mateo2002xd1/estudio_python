from database import Base
from sqlalchemy import Column, Integer, String

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True, nullable=False)
    usuario = Column(String, nullable=True)
    password_hash  = Column(String, nullable=True)
    nombre = Column(String, index=True, nullable=True)
    edad = Column(Integer, nullable=False)