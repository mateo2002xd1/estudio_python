from pydantic import BaseModel, Field
from typing import Optional

class UsuarioCrear(BaseModel):
    
    id: int = Field(gt=0)
    edad: int = Field(gt=0)
    nombre: str = Field(min_length=1)

class UsuarioRegistro(BaseModel):
    
    id: int = Field(gt=0)
    usuario: str = Field(min_length=1)
    password_hash: str = Field(min_length=1)

class UsuarioLogin(BaseModel):
    
    id: int = Field(gt=0)
    usuario: str = Field(min_length=1)
    password_hash: str = Field(min_length=1)

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    edad: int
    usuario: Optional[str] = None

    class Config:
        from_attributes = True