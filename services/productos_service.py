from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.productos_db import Producto
from schemas.productos_schema import ProductoInput, ProductoResponse 

def ingresar_producto(producto_test: ProductoInput, db: Session):
    existe = db.query(Producto).filter(
        Producto.codigo == producto_test.codigo
    ).first()

    if existe:
        raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Producto repetido"
                )
    data = producto_test.model_dump()

    nuevo = Producto(
        **data
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def mostrar_productos(db: Session):
    return db.query(Producto).all()

def mostrar_producto_codigo(codigo: int, db: Session):
    existe = db.query(Producto).filter(
        Producto.codigo == codigo
    ).first()
    
    if existe:
        return existe
    raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Producto no encontrado"
                )

def reemplazar_producto(codigo: int, producto_body: ProductoInput, db: Session):  
    producto = db.query(Producto).filter(
       Producto.codigo == codigo
    ).first()

    if producto:
        producto.nombre = producto_body.nombre
        producto.precio = producto_body.precio

        db.commit()
        db.refresh(producto)
        return producto
    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="Producto no encontrado"
                    )

def eliminar_producto(codigo: int, db: Session):
    producto = db.query(Producto).filter(
        Producto.codigo == codigo
    ).first()
    
    if not producto:
        raise HTTPException(
                            status_code=status.HTTP_404_NOT_FOUND,
                            detail="Producto no encontrado"
                        )
    
    db.delete(producto)
    db.commit()

    return  producto