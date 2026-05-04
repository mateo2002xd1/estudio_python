from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.core.config import SECRET_KEY, ALGORITHM
from app.database import get_db
from app.core.exceptions import UsuarioYaNoExiste, TokenInvalido
from app.repositories.usuarios_repositories import consultar_usuario_db

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario = consultar_usuario_db(int(payload["sub"]), db)
        if usuario:    
            return usuario
        raise UsuarioYaNoExiste()
    except JWTError:
        raise TokenInvalido()