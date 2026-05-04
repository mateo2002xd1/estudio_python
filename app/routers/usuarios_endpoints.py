from fastapi import APIRouter, Depends, HTTPException, status
from app.services.usuarios_service import ingreso_usuario
from app.schemas.usuarios_schema import UsuarioCrear, UsuarioResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.exceptions import UsuarioRepetido

router = APIRouter(prefix="/api/usuarios")

@router.post("/", response_model=UsuarioResponse)
def ingreso_usuario_endpoint(usuario_ingresar: UsuarioCrear, db: Session = Depends(get_db)):
    try:
        return ingreso_usuario(usuario_ingresar, db)
    except UsuarioRepetido:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Usuario ya existe"
            )