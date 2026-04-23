from fastapi import FastAPI, Query, APIRouter

var_mensaje : str

app = FastAPI()

router = APIRouter(prefix="/api")

@router.get("/") 
def read_root():
    var_mensaje = "Hola mundo"
    return {"mensaje": var_mensaje}

@router.get("/saludo")
def saludo():
    var_mensaje = "mateo"
    return {"mensaje": var_mensaje}

@router.get("/usuario/{id}")
def info_parameter(id: int):
    if id == 1:
        var_mensaje = "Mateo"
    elif id == 2:
        var_mensaje = "Sebastian"
    else:
        var_mensaje = "User not Found"

    return {"mensaje": var_mensaje }

@router.get("/buscar")
def buscar(nombre: str | None = Query(default=None)):
    if nombre is None:
        var_mensaje = ""
    else:
        var_mensaje = nombre
    return {"mensaje": var_mensaje }

@router.get("/producto/{id}")
def info_parameter(id: int | None):
    if id == 1:
        var_mensaje = "Arroz"
    elif id == 2:
        var_mensaje = "Leche"
    else:
        var_mensaje = "Producto no existe12"

    return {"mensaje": var_mensaje }


app.include_router(router)