from models.productos import usuario

def post_ingreso_usuario(usuario_recibe: usuario):
    return {"status": "ok", "data": usuario_recibe}