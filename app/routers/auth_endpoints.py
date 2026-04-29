from fastapi import APIRouter, Depends
from app.auth.auth_service import login_usuario, registro_usuario
from app.schemas.usuarios_schema import UsuarioResponse, UsuarioRegistro, UsuarioLogin
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter(prefix="/auth/usuarios")

@router.patch("/{id}/registro/", response_model=UsuarioResponse)
def registro_usuario_endpoint(id: int, usuario_registro: UsuarioRegistro, db: Session = Depends(get_db)):
    return registro_usuario(id, usuario_registro, db)

@router.post("/{id}/login/", response_model=UsuarioResponse)
def login_usuario_endpoint(id: int, usuario_login: UsuarioLogin, db: Session = Depends(get_db)):
    return login_usuario(id, usuario_login, db)