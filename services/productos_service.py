from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.productos import Producto, ProductoCreate

def ingresar_producto(producto_test: ProductoCreate, db: Session):
    existe = db.query(Producto).filter(
        Producto.codigo == producto_test.codigo
    ).first()

    if existe:
        raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Producto repetido"
                )
    data = producto_test.dict()

    nuevo = Producto(
        **data
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return {
            "status": "ok",
            "data": nuevo,
            "message": "Se guardó correctamente el producto"
        }

def mostrar_productos(db: Session):
    return {
        "status": "ok",
        "data": db.query(Producto).all(),
        "message": "Lista completa de productos"
    }

def mostrar_producto_codigo(codigo: int, db: Session):
    existe = db.query(Producto).filter(
        Producto.codigo == codigo
    ).first()
    
    if existe:
        return {
                "status": "ok",
                "data": existe,
                "message": f"Producto codigo: {codigo}"
            }
    raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Producto no encontrado"
                )

def reemplazar_producto(codigo: int, producto_body: ProductoCreate, db: Session):  
    producto = db.query(Producto).filter(
       Producto.codigo == codigo
    ).first()

    if producto:
        producto.nombre = producto_body.nombre
        producto.precio = producto_body.precio

        db.commit()
        db.refresh(producto)
        return {
            "status": "ok",
            "data": producto,
            "message": f"Reemplazo del Producto codigo: {codigo}"
        }
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

    return {
        "status": "ok",
        "data": [],
        "message": "Se elimino el producto"
    }