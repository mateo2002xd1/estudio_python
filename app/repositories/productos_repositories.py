from sqlalchemy.orm import Session, Query
from app.models.productos_db import Producto

def preparar_consulta_productos(db: Session):
    return db.query(Producto)

def commit_products(db: Session):
    db.commit()

def refrescar_producto(producto: Producto, db: Session):
    return db.refresh(producto)

def eliminar_producto_db(producto: Producto, db: Session):
    db.delete(producto)
    commit_products(db)
    return producto

def consultar_producto_db(codigo: int, db: Session):
    return preparar_consulta_productos(db).filter(
        Producto.codigo == codigo
    ).first()

def ingresar_producto_db(nuevo_producto: Producto, db: Session):
    db.add(nuevo_producto)
    commit_products(db)
    refrescar_producto(nuevo_producto, db)
    return nuevo_producto

def agregar_filtro_nombre_productos(query_productos: Query[Producto], nombre: str):
    return query_productos.filter(
        Producto.nombre.like(nombre)
    )

def agregar_filtro_precio_min_productos(query_productos: Query[Producto], precio_min: float):
    return query_productos.filter(
        Producto.precio >= precio_min
    )

def agregar_filtro_precio_max_productos(query_productos: Query[Producto], precio_max: float):
    return query_productos.filter(
            Producto.precio <= precio_max
        )

def agregar_offset_productos(query_productos: Query[Producto], skip: int):
    return query_productos.offset(skip)

def agregar_limit_productos(query_productos: Query[Producto], limit_db: int):
    return query_productos.limit(limit_db)

def realizar_busqueda_completa_productos(query_productos: Query[Producto]):
    return query_productos.all()