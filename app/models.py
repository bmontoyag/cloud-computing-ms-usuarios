from pydantic import BaseModel

class UsuarioIn(BaseModel):
    nombre: str
    email: str
    telefono: str
    rol_id: int
    estado: bool = True
