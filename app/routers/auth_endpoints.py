from fastapi import APIRouter, Depends, HTTPException, status
from app.auth.auth_service import login_usuario, registro_usuario
from app.schemas.usuarios_schema import UsuarioResponse, UsuarioRegistro, UsuarioLogin, TokenResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.exceptions import UsuarioNoEncontrado, UsuarioRepetido, UsuarioYaNoExiste, TokenInvalido, PasswordInvalida, UsuarioYaExiste

router = APIRouter(prefix="/auth/usuarios")

@router.patch("/{id}/registro/", response_model=UsuarioResponse)
def registro_usuario_endpoint(id: int, usuario_registro: UsuarioRegistro, db: Session = Depends(get_db)):
    try:
        return registro_usuario(id, usuario_registro, db)
    except UsuarioNoEncontrado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no Encontrado"
            )    
    except UsuarioYaNoExiste:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario ya no Existe"
            )    
    except UsuarioYaExiste:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Usuario ya Existe"
            )   
    except UsuarioRepetido:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Usuario ya esta Registrado"
            )     
    except TokenInvalido:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token Invalido"
            ) 
    except PasswordInvalida:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales Incorrectas"
            ) 
        
@router.post("/{id}/login/", response_model=TokenResponse)
def login_usuario_endpoint(id: int, usuario_login: UsuarioLogin, db: Session = Depends(get_db)):
    try:
        return login_usuario(id, usuario_login, db)
    except UsuarioNoEncontrado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario no Encontrado"
            )    
    except UsuarioYaNoExiste:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuario ya no Existe"
            )    
    except UsuarioYaExiste:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Usuario ya Existe"
            )   
    except TokenInvalido:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token Invalido"
            ) 
    except UsuarioRepetido:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Usuario ya esta Registrado"
            )     
    except PasswordInvalida:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales Incorrectas"
            ) 