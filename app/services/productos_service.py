from sqlalchemy.orm import Session
from app.models.productos_db import Producto
from app.schemas.productos_schema import ProductoInput, ProductoFiltro
from app.core.logger import logger
from app.repositories.productos_repositories import (
        consultar_producto_db,
        commit_products,
        refrescar_producto,
        eliminar_producto_db,
        ingresar_producto_db,
        preparar_consulta_productos,
        agregar_filtro_nombre_productos,
        agregar_filtro_precio_min_productos,
        agregar_filtro_precio_max_productos,
        agregar_offset_productos,
        agregar_limit_productos,
        realizar_busqueda_completa_productos
    )
from app.core.exceptions import ProductoNoEncontrado, ProductoRepetido

def ingresar_producto(producto_test: ProductoInput, db: Session):
    existe = consultar_producto_db(producto_test.codigo, db)

    if existe:
        logger.error("409. Producto repetido")
        raise ProductoRepetido()
    data = producto_test.model_dump()

    nuevo = Producto(
        **data
    )
    nuevo = ingresar_producto_db(nuevo, db)
    
    logger.info("200. Producto registrado")
    return nuevo

def mostrar_productos_codigo(codigo: int, db: Session):
    productos = consultar_producto_db(codigo, db)
    
    if productos:
        logger.info("200. Productos filtrados")
        return productos
    
    logger.error("404. Producto no encontrado")
    raise ProductoNoEncontrado()

def mostrar_producto_filtros(
        db: Session,
        nombre: str | None = None,
        precio_min: float | None = None,
        precio_max: float | None = None,
        skip: int = 0,
        limit: int = 10
        ):  

    productos = preparar_consulta_productos(db)
    
    if nombre is not None:
        productos = agregar_filtro_nombre_productos(productos, f"%{nombre}%")
    
    if precio_min is not None:
        productos = agregar_filtro_precio_min_productos(productos, precio_min)
    
    if precio_max is not None:
        productos = agregar_filtro_precio_max_productos(productos, precio_max)

    if skip is not None:
        productos = agregar_offset_productos(productos, skip)

    if limit is not None:
        productos = agregar_limit_productos(productos, limit)

    productos = realizar_busqueda_completa_productos(productos)

    if productos:
        logger.info("200. Productos filtrados")
        return productos
    
    logger.error("404. Productos no encontrado")
    raise ProductoNoEncontrado()

def reemplazar_producto(codigo: int, producto_body: ProductoInput, db: Session):  
    producto = consultar_producto_db(codigo, db)

    if producto:
        producto.nombre = producto_body.nombre
        producto.precio = producto_body.precio

        commit_products(db)
        refrescar_producto(producto, db)
        
        logger.info("200. Producto reemplazado")
        return producto
    
    logger.error("404. Producto no encontrado")
    raise ProductoNoEncontrado()

def eliminar_producto(codigo: int, db: Session):
    producto = consultar_producto_db(codigo, db)
    
    if not producto:
        logger.error("404. Producto no encontrado")
        raise ProductoNoEncontrado()
    
    eliminar_producto_db(producto, db)

    logger.info("200. Producto eliminado")
    return  producto