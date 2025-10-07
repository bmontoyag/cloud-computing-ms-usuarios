
from fastapi import FastAPI
from app.db import engine
from app.models.base import Base
from app.util.cors import add_cors

app = FastAPI(title="Servicio API")

# Crear tablas (solo demo)
Base.metadata.create_all(bind=engine)

@app.get("/health")
def health():
    return {"status": "ok"}

from app.routers import usuario
app.include_router(usuario.router)
