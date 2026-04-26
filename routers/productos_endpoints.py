from fastapi import APIRouter, Depends
from services.productos_service import (
    ingresar_producto,
    mostrar_productos,
    mostrar_producto_codigo,
    reemplazar_producto,
    eliminar_producto
)
from models.productos import ProductoCreate
from database import get_db
from sqlalchemy.orm import Session

DBSession = Depends(get_db)

router = APIRouter(prefix="/productos")


@router.post("/")
def ingresar_producto_endpoint(producto_test: ProductoCreate, db: Session = DBSession):
        return ingresar_producto(producto_test, db)

@router.get("/")
def mostrar_productos_endpoint(db: Session = DBSession):
        return mostrar_productos(db)

@router.get("/{codigo}")
def mostrar_producto_codigo_endpoint(codigo: int, db: Session = DBSession):
    return mostrar_producto_codigo(codigo, db)

@router.put("/{codigo}")
def reemplazar_producto_endpoint(codigo: int, producto_body: ProductoCreate, db: Session = DBSession):
    return reemplazar_producto(codigo, producto_body, db)

@router.delete("/{codigo}")
def eliminar_producto_endpoint(codigo: int, db: Session = DBSession):
      return eliminar_producto(codigo, db)