from models.productos import usuario

def ingreso_usuario(usuario_recibe: usuario):
    if not usuario_recibe.nombre:
        return {"status": "error", "data": [], "message": "Nombre esta vacio"}   
    if usuario_recibe.edad < 0:
        return {"status": "error", "data": [], "message": "Edad es negativa"}   
    return {"status": "ok", "data": usuario_recibe, "message": "test"}   