from fastapi import APIRouter
from services.usuarios_service import usuario, post_ingreso_usuario

router = APIRouter(prefix="/usuarios")

@router.post("/ingresar")
def post_ingreso_usuario_endpoint(usuario_ingresar: usuario):
    return post_ingreso_usuario(usuario_ingresar)