from sqlalchemy.orm import Session
from app.models.usuarios_db import Usuario

def consultar_usuario_db(id: int, db: Session):
    return db.query(Usuario).filter(
        Usuario.id == id
    ).first()

def insertar_usuario_db(nuevo: Usuario, db: Session):
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return nuevo

def actualizar_usuario(usuario_act: Usuario, db: Session):
    db.commit()
    db.refresh(usuario_act)