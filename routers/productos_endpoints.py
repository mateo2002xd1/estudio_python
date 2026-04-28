from fastapi import APIRouter, Depends
from services.productos_service import (
    ingresar_producto,
    mostrar_productos_codigo,
    mostrar_producto_filtros,
    reemplazar_producto,
    eliminar_producto
)
from schemas.productos_schema import ProductoInput, ProductoResponse
from database import get_db
from sqlalchemy.orm import Session
from auth.auth_dependencia import get_current_user

router = APIRouter(prefix="/api/productos")

@router.post("/", response_model=ProductoResponse)
def ingresar_producto_endpoint(producto_test: ProductoInput, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return ingresar_producto(producto_test, db)

@router.get("/{codigo}", response_model=ProductoResponse)
def mostrar_productos_codigo_endpoint(codigo: int, db: Session = Depends(get_db)):
    return mostrar_productos_codigo(codigo, db)

@router.get("/", response_model=list[ProductoResponse])
def mostrar_producto_filtros_endpoint(
        db: Session = Depends(get_db),
        nombre: str | None = None,
        precio_min: float | None = None,
        precio_max: float | None = None,
        skip: int = 0,
        limit: int = 10
    ):

    return mostrar_producto_filtros(db, nombre, precio_min, precio_max, skip, limit)

@router.put("/{codigo}", response_model=ProductoResponse)
def reemplazar_producto_endpoint(codigo: int, producto_body: ProductoInput, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return reemplazar_producto(codigo, producto_body, db)

@router.delete("/{codigo}", response_model=ProductoResponse)
def eliminar_producto_endpoint(codigo: int, db: Session = Depends(get_db), user = Depends(get_current_user)):
    return eliminar_producto(codigo, db)