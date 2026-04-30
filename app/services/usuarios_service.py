from app.schemas.usuarios_schema import UsuarioCrear
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.usuarios_db import Usuario
from app.core.logger import logger

def ingreso_usuario(usuario_ingresar: UsuarioCrear, db: Session):
    existe = db.query(Usuario).filter(
        Usuario.id == usuario_ingresar.id
    ).first()

    if existe:
        logger.error("409. Usuario ya existe")
        raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Usuario ya existe"
                )
    
    data = usuario_ingresar.model_dump()

    nuevo = Usuario(
        **data
    )
    nuevo.usuario = nuevo.id
    
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    
    logger.error("200. Usuario creado")
    return nuevo