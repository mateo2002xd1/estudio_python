from pydantic import BaseModel, Field
from typing import Optional

class UsuarioCrear(BaseModel):
    
    id: int = Field(gt=0)
    edad: int = Field(gt=0)
    nombre: str = Field(min_length=1)

class UsuarioRegistro(BaseModel):
    
    password: str = Field(min_length=4)

class UsuarioLogin(BaseModel):
    
    password: str = Field(min_length=4)

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    edad: int
    usuario: int

    class Config:
        from_attributes = True