from fastapi import APIRouter
<<<<<<< HEAD
from services.usuarios_service import usuario, post_ingreso_usuario

router = APIRouter(prefix="/usuarios")

@router.post("/ingresar")
def post_ingreso_usuario_endpoint(usuario_ingresar: usuario):
    return post_ingreso_usuario(usuario_ingresar)
=======
from services.usuarios_service import ingreso_usuario
from models.productos import usuario

router = APIRouter(prefix="/usuarios")

@router.post("/")
def ingreso_usuario_endpoint(usuario_ingresar: usuario):
    return ingreso_usuario(usuario_ingresar)
>>>>>>> c56ca4bb137baba9beda49c920459f7606142854
