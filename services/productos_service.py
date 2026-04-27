from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.productos_db import Producto
from schemas.productos_schema import ProductoInput 

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

def mostrar_productos_codigo(codigo: int, db: Session):
    productos = db.query(Producto).filter(Producto.codigo == codigo).first()
    
    if productos:
        return productos
    
    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="Producto no encontrado"
                    )

def mostrar_producto_filtros(
        db: Session,
        nombre: str | None = None,
        precio_min: float | None = None,
        precio_max: float | None = None,
        skip: int = 0,
        limit: int = 10
        ):  

    productos = db.query(Producto)
    
    if nombre is not None:
        productos = productos.filter(
            Producto.nombre.like(f"%{nombre}%")
        ).order_by(Producto.nombre)
    
    if precio_min is not None:
        productos = productos.filter(
            Producto.precio >= precio_min
        ).order_by(Producto.precio)
    
    if precio_max is not None:
        productos = productos.filter(
            Producto.precio <= precio_max
        ).order_by(Producto.precio)

    if skip is not None:
        productos = productos.offset(skip)

    if limit is not None:
        productos = productos.limit(limit)

    productos = productos.all()

    if productos:
        return productos
    
    raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND,
                        detail="Productos no encontrado"
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