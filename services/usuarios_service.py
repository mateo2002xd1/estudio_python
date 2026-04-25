from models.productos import usuario
from fastapi import HTTPException

def ingreso_usuario(usuario_recibe: usuario):
    if not usuario_recibe.nombre:
        raise HTTPException(
            status_code=400,
            detail="Producto repetido"
        )
    if usuario_recibe.edad < 0:
        raise HTTPException(
            status_code=400,
            detail="Edad es negativa"
        )
    return {
            "status": "ok",
            "data": usuario_recibe,
            "message": "Usuario ingresado"
        }