
from pydantic import BaseModel, EmailStr

class UsuarioCreate(BaseModel):
    email: EmailStr
    nombre: str
    rol: str | None = "empleado"

class UsuarioOut(UsuarioCreate):
    id: int
    class Config:
        from_attributes = True
