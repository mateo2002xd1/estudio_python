from fastapi import APIRouter
from services.usuarios_service import post_ingreso_usuario
from models.productos import usuario

router = APIRouter(prefix="/usuarios")

@router.post("/")
def post_ingreso_usuario_endpoint(usuario_ingresar: usuario):
    return post_ingreso_usuario(usuario_ingresar)