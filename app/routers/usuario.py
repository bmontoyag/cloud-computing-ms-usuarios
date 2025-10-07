
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioOut

router = APIRouter(prefix="/usuarios", tags=["usuarios"])

@router.get("/", response_model=list[UsuarioOut])
def list_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@router.post("/", response_model=UsuarioOut)
def create_usuario(payload: UsuarioCreate, db: Session = Depends(get_db)):
    exists = db.query(Usuario).filter_by(email=payload.email).first()
    if exists:
        raise HTTPException(status_code=409, detail="Email ya registrado")
    user = Usuario(email=payload.email, nombre=payload.nombre, rol=payload.rol or "empleado")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
