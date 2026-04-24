from fastapi import APIRouter
from services.usuarios_service import ingreso_usuario
from models.productos import usuario

router = APIRouter(prefix="/usuarios")

@router.post("/")
def ingreso_usuario_endpoint(usuario_ingresar: usuario):
    return ingreso_usuario(usuario_ingresar)