from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import time

DATABASE_URL = "postgresql+psycopg2://postgres:1234@db:5432/fastapi_db"

# 🔥 Retry para esperar a PostgreSQL
for i in range(10):
    try:
        engine = create_engine(
            DATABASE_URL,
            echo=False
        )
        # intenta conectar
        connection = engine.connect()
        connection.close()
        print("✅ Conectado a PostgreSQL")
        break
    except Exception as e:
        print(f"⏳ Esperando DB... intento {i+1}")
        time.sleep(2)
else:
    raise Exception("❌ No se pudo conectar a la base de datos")

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()