from sqlalchemy.orm import Session
from app.models.usuarios_db import Usuario
from app.schemas.usuarios_schema import UsuarioRegistro, UsuarioLogin
from passlib.context import CryptContext
from fastapi import HTTPException, status
from jose import jwt
from app.config import SECRET_KEY, ALGORITHM, EXPIRACION_MINUTOS
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def crear_token(data: dict):
    to_create = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=EXPIRACION_MINUTOS)

    to_create.update({"exp": expire})

    token = jwt.encode(to_create, SECRET_KEY, algorithm=ALGORITHM)

    return token

def usuario_consulta(id: int, db: Session):
    return db.query(Usuario).filter(Usuario.id == id).first()

def registro_usuario(id: int, usuario_registro: UsuarioRegistro, db: Session):
    usuario = usuario_consulta(id, db)
    
    if usuario:
        if usuario.password_hash is not None:
                raise HTTPException(
                        status_code=status.HTTP_409_CONFLICT,
                        detail="Usuario ya esta registrado"
                    )    
        
        hash_password = pwd_context.hash(usuario_registro.password)
        usuario.password_hash = hash_password
        db.commit()
        db.refresh(usuario)
        
        return usuario

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )

def login_usuario(id: int, usuario_login: UsuarioLogin, db: Session):
    usuario = usuario_consulta(id, db)
    
    if usuario:
        if usuario.password_hash is None:
                raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Usuario no esta registrado"
                    )  
        if pwd_context.verify(usuario_login.password, usuario.password_hash):
            print(crear_token({"sub": str(usuario.id)}))
            return usuario
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Contraseña no es correcta"
        )
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )