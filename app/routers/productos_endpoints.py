from fastapi import APIRouter, Depends, Path, HTTPException, status
from app.services.productos_service import (
    ingresar_producto,
    mostrar_productos_codigo,
    mostrar_producto_filtros,
    reemplazar_producto,
    eliminar_producto
)
from app.schemas.productos_schema import ProductoInput, ProductoResponse
from app.database import get_db
from sqlalchemy.orm import Session
from app.auth.auth_dependencia import get_current_user
from app.core.exceptions import ProductoNoEncontrado, ProductoRepetido, TokenInvalido, UsuarioYaNoExiste


router = APIRouter(prefix="/api/productos")

@router.post("/", response_model=ProductoResponse)
def ingresar_producto_endpoint(producto_test: ProductoInput, db: Session = Depends(get_db), user = Depends(get_current_user)):
    try:
        return ingresar_producto(producto_test, db)
    except ProductoRepetido:
            raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Producto Repetido"
                )
    except TokenInvalido:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token Invalido"
            ) 
    except UsuarioYaNoExiste:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario ya no Existe"
        ) 

@router.get("/{codigo}", response_model=ProductoResponse)
def mostrar_productos_codigo_endpoint(codigo: int = Path(gt=0), db: Session = Depends(get_db)):
    try:
        return mostrar_productos_codigo(codigo, db)
    except ProductoNoEncontrado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Producto No Encontrado"
            )

@router.get("/", response_model=list[ProductoResponse])
def mostrar_producto_filtros_endpoint(
        db: Session = Depends(get_db),
        nombre: str | None = None,
        precio_min: float | None = None,
        precio_max: float | None = None,
        skip: int = 0,
        limit: int = 10
    ):

    try:
        return mostrar_producto_filtros(db, nombre, precio_min, precio_max, skip, limit)
    except ProductoNoEncontrado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Producto No Encontrado"
            )

@router.put("/{codigo}", response_model=ProductoResponse)
def reemplazar_producto_endpoint(codigo: int, producto_body: ProductoInput, db: Session = Depends(get_db), user = Depends(get_current_user)):
    try:
        return reemplazar_producto(codigo, producto_body, db)
    except ProductoNoEncontrado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Producto No Encontrado"
            )
    except TokenInvalido:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token Invalido"
            ) 
    except UsuarioYaNoExiste:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario ya no Existe"
        ) 

@router.delete("/{codigo}", response_model=ProductoResponse)
def eliminar_producto_endpoint(codigo: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    try:
        return eliminar_producto(codigo, db)
    except ProductoNoEncontrado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Producto No Encontrado"
            )