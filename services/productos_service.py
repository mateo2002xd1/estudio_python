from models.productos import producto

productos_db = []

def post_ingresar_producto(producto_test: producto):
    for u in productos_db:
        if u.codigo == producto_test.codigo:
            return {"status": "error","message": "Producto repetido"}
    productos_db.append(producto_test)
    return {"status": "ok", "data": "Se guardo correctamente el producto"}

def get_mostrar_productos():
    return {"status": "ok", "data": productos_db}

def get_mostrar_producto_codigo(codigo: int):
    for test_producto in productos_db:
        if test_producto.codigo == codigo:
            return {"status": "ok", "data": test_producto}
    return {"status": "error","message": "no encontrado"}

def put_reemplazar_producto(codigo: int, producto_body: producto):  
    producto_correcto = producto_body.model_copy()
    producto_correcto.codigo = codigo
    for i, producto_buscar in enumerate(productos_db):
        if producto_buscar.codigo == codigo:
            productos_db[i] = producto_correcto
            return {"status": "ok", "data": productos_db[i]}
    return {"status": "error","message": "no encontrado"}


def delete_eliminar_producto(codigo: int):
    producto_existe = next((p for p in productos_db if p.codigo == codigo), None)
    if not producto_existe:
        return {"status": "error","message": "no encontrado"}
    productos_db.remove(producto_existe)
    return {"status": "ok", "data": "Se elimino el producto"}