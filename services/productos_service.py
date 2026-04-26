from fastapi import HTTPException
from models.productos import ProductoCreate, productos_db

def ingresar_producto(producto_test: ProductoCreate):
    for u in productos_db:
        if u.codigo == producto_test.codigo:
            raise HTTPException(
                status_code=400,
                detail="Producto repetido"
            )
    productos_db.append(producto_test)
    return {
        "status": "ok",
        "data": producto_test,
        "message": "Se guardó correctamente el producto"
    }

def mostrar_productos():
    return {
        "status": "ok",
        "data": productos_db,
        "message": "Lista completa de productos"
    }

def mostrar_producto_codigo(codigo: int):
    for test_producto in productos_db:
        if test_producto.codigo == codigo:
            return {
                "status": "ok",
                "data": test_producto,
                "message": f"Producto codigo: {codigo}"
            }
    raise HTTPException(
                    status_code=400,
                    detail="Producto no encontrado"
                )

def reemplazar_producto(codigo: int, producto_body: ProductoCreate):  
    producto_correcto = producto_body.model_copy()
    producto_correcto.codigo = codigo
    for i, producto_buscar in enumerate(productos_db):
        if producto_buscar.codigo == codigo:
            productos_db[i] = producto_correcto
            return {
                    "status": "ok",
                    "data": productos_db[i],
                    "message": f"Reemplado del Producto codigo: {codigo}"
                }
    raise HTTPException(
                        status_code=400,
                        detail="Producto no encontrado"
                    )


def eliminar_producto(codigo: int):
    producto_existe = next((p for p in productos_db if p.codigo == codigo), None)
    if not producto_existe:
        raise HTTPException(
                            status_code=400,
                            detail="Producto no encontrado"
                        )
    productos_db.remove(producto_existe)
    return {
        "status": "ok",
        "data": [],
        "message": "Se elimino el producto"
    }