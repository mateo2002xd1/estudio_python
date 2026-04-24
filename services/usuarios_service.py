from models.productos import usuario

def post_ingreso_usuario(usuario_recibe: usuario):
    if not usuario_recibe.nombre:
        return {"status": "error","message": "Nombre esta vacio"}
    if usuario_recibe.edad < 0:
        return {"status": "error","message": "Edad es negativa"}
    return {"status": "ok", "data": usuario_recibe}