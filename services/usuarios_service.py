from schemas.usuarios_schema import UsuarioCrear
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.usuarios_db import Usuario

def ingreso_usuario(usuario_ingresar: UsuarioCrear, db: Session):
    existe = db.query(Usuario).filter(
        Usuario.id == usuario_ingresar.id
    ).first()

    if existe:
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

    return nuevo