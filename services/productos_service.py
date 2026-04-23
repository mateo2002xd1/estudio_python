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