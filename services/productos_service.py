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
    return {
            "status": "ok",
            "data": producto_test,
            "message": "Se guardó correctamente el producto"
        }

def mostrar_productos(db: Session):
    return {
        "status": "ok",
        "data": db.query(Producto).all(),
        "message": "Lista completa de productos"
    }

def mostrar_producto_codigo(codigo: int, db = Session):
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
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Producto no encontrado"
                )

def reemplazar_producto(codigo: int, producto_body: ProductoCreate, db = Session):  
    existe = db.query(Producto).filter(
       Producto.codigo == codigo
    ).first()

    if existe:
        db.query(Producto).filter(
            Producto.codigo == codigo
        ).update({
                    Producto.nombre: producto_body.nombre,
                    Producto.precio: producto_body.precio
                })
        db.commit()
        return {
            "status": "ok",
            "data": db.query(Producto).filter(Producto.codigo == codigo).first(),
            "message": f"Reemplazo del Producto codigo: {codigo}"
        }
    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Producto no encontrado"
                    )

def eliminar_producto(codigo: int, db: Session):
    existe = db.query(Producto).filter(
        Producto.codigo == codigo
    ).first()
    
    if not existe:
        raise HTTPException(
                            status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Producto no encontrado"
                        )
    
    db.query(Producto).filter(
        Producto.codigo == codigo
    ).delete()

    db.commit()

    return {
        "status": "ok",
        "data": [],
        "message": "Se elimino el producto"
    }