from fastapi import APIRouter
from services.usuarios_service import ingreso_usuario
from schemas.productos_schema import UsuarioInput

router = APIRouter(prefix="/api/usuarios")

@router.post("/")
def ingreso_usuario_endpoint(usuario_ingresar: UsuarioInput):
    return ingreso_usuario(usuario_ingresar)