from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.core.config import SECRET_KEY, ALGORITHM
from app.database import get_db
from app.models.usuarios_db import Usuario

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario = db.query(Usuario).filter(Usuario.id == int(payload["sub"])).first()
        if usuario:    
            return usuario
        raise HTTPException(status_code=401, detail="Usuario ya no existe")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")