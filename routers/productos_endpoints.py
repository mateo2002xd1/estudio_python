from fastapi import APIRouter, Depends
from services.productos_service import (
    ingresar_producto,
    mostrar_productos,
    mostrar_producto_codigo,
    reemplazar_producto,
    eliminar_producto
)
from schemas.productos_schema import ProductoInput, ProductoResponse
from database import get_db_productos
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/productos")


@router.post("/", response_model=ProductoResponse)
def ingresar_producto_endpoint(producto_test: ProductoInput, db: Session = Depends(get_db_productos)):
        return ingresar_producto(producto_test, db)

@router.get("/", response_model=list[ProductoResponse])
def mostrar_productos_endpoint(db: Session = Depends(get_db_productos)):
        return mostrar_productos(db)

@router.get("/{codigo}", response_model=ProductoResponse)
def mostrar_producto_codigo_endpoint(codigo: int, db: Session = Depends(get_db_productos)):
    return mostrar_producto_codigo(codigo, db)

@router.put("/{codigo}", response_model=ProductoResponse)
def reemplazar_producto_endpoint(codigo: int, producto_body: ProductoInput, db: Session = Depends(get_db_productos)):
    return reemplazar_producto(codigo, producto_body, db)

@router.delete("/{codigo}", response_model=ProductoResponse)
def eliminar_producto_endpoint(codigo: int, db: Session = Depends(get_db_productos)):
      return eliminar_producto(codigo, db)