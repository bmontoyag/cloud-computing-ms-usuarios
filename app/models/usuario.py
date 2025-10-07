
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    __table_args__ = {"schema": "usuarios"}
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    nombre: Mapped[str] = mapped_column(String(120))
    rol: Mapped[str] = mapped_column(String(50), default="empleado")
