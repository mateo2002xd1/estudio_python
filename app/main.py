from fastapi import FastAPI
from app.routers.productos_endpoints import router as productos_router
from app.routers.auth_endpoints import router as auth_router
from app.routers.usuarios_endpoints import router as usuarios_router
from app.database import Base, engine
from sqlalchemy import text
import time

app = FastAPI()

def init_db():
    for i in range(10):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))

            Base.metadata.create_all(bind=engine)
            print("✅ DB lista y tablas creadas")
            return

        except Exception as e:
            print(f"⏳ Esperando DB... intento {i+1}")
            time.sleep(2)

    raise Exception("❌ No se pudo conectar a la DB")

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(productos_router)
app.include_router(usuarios_router)
app.include_router(auth_router)