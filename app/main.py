from fastapi import FastAPI
from mangum import Mangum
from app.routes.usuarios import router as usuarios_router

app = FastAPI(
    title="Microservicio de Usuarios",
    version="1.0.0",
    description="Gestión de cuentas de empleados y clientes para el sistema de cotizaciones"
)

app.include_router(usuarios_router, prefix="/api/usuarios", tags=["Usuarios"])
handler = Mangum(app)
