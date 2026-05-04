from app.schemas.usuarios_schema import UsuarioCrear
from sqlalchemy.orm import Session
from app.models.usuarios_db import Usuario
from app.core.logger import logger
from app.repositories.usuarios_repositories import (
    consultar_usuario_db,
    insertar_usuario_db
)
from app.core.exceptions import UsuarioRepetido

def ingreso_usuario(usuario_ingresar: UsuarioCrear, db: Session):
    existe = consultar_usuario_db(usuario_ingresar.id, db)

    if existe:
        logger.error("409. Usuario ya existe")
        raise UsuarioRepetido()
    
    data = usuario_ingresar.model_dump()

    nuevo = Usuario(
        **data
    )
    nuevo.usuario = nuevo.id
    
    nuevo = insertar_usuario_db(nuevo, db)
    
    logger.error("200. Usuario creado")
    return nuevo