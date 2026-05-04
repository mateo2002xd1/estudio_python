from sqlalchemy.orm import Session
from app.schemas.usuarios_schema import UsuarioRegistro, UsuarioLogin
from passlib.context import CryptContext
from jose import jwt
from app.core.config import SECRET_KEY, ALGORITHM, EXPIRACION_MINUTOS
from datetime import datetime, timedelta
from app.core.logger import logger
from app.repositories.usuarios_repositories import consultar_usuario_db, actualizar_usuario
from app.core.exceptions import UsuarioRepetido, UsuarioNoEncontrado, PasswordInvalida, UsuarioYaExiste
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def crear_token(data: dict):
    to_create = data.copy()
    
    expire = datetime.utcnow() + timedelta(minutes=EXPIRACION_MINUTOS)

    to_create.update({"exp": expire})

    token = jwt.encode(to_create, SECRET_KEY, algorithm=ALGORITHM)
    
    logger.info("200. Token generado")
    return token

def registro_usuario(id: int, usuario_registro: UsuarioRegistro, db: Session):
    usuario = consultar_usuario_db(id, db)
    
    if usuario:
        if usuario.password_hash is not None:
                logger.error("409. Usuario ya esta registrado")
                raise UsuarioRepetido()
        
        hash_password = pwd_context.hash(usuario_registro.password)
        usuario.password_hash = hash_password
        actualizar_usuario(usuario, db)
        
        logger.info("200. Usuario registrado")
        return usuario
    
    logger.error("409. Usuario ya esta registrado")
    raise UsuarioRepetido()

def login_usuario(id: int, usuario_login: UsuarioLogin, db: Session):
    usuario = consultar_usuario_db(id, db)
    
    if usuario:
        if usuario.password_hash is None:
                logger.error("400. Usuario no esta registrado")
                raise UsuarioNoEncontrado()
        if pwd_context.verify(usuario_login.password, usuario.password_hash):
            token = crear_token({"sub": str(usuario.id)})
            return {
                "access_token": token,
                "token_type": "bearer"
            }
        
        logger.error("401. Contraseña no es correcta")
        raise PasswordInvalida()
    
    logger.error("404. Usuario registrado")
    raise UsuarioNoEncontrado()