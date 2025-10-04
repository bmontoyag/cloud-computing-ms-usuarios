from fastapi import APIRouter, HTTPException
from app.database import get_connection
from app.models import UsuarioIn

router = APIRouter()

@router.get("/")
def listar_usuarios():
    conn, cur = get_connection()
    try:
        cur.execute("SELECT id_usuario, nombre, email, telefono, estado FROM usuarios;")
        usuarios = [
            {"id": r[0], "nombre": r[1], "email": r[2], "telefono": r[3], "estado": r[4]}
            for r in cur.fetchall()
        ]
        return usuarios
    finally:
        conn.close()

@router.post("/")
def crear_usuario(usuario: UsuarioIn):
    conn, cur = get_connection()
    try:
        cur.execute(
            """
            INSERT INTO usuarios (nombre, email, telefono, rol_id, estado)
            VALUES (%s,%s,%s,%s,%s) RETURNING id_usuario;
            """,
            (usuario.nombre, usuario.email, usuario.telefono, usuario.rol_id, usuario.estado)
        )
        nuevo_id = cur.fetchone()[0]
        conn.commit()
        return {"mensaje": "Usuario creado correctamente", "id_usuario": nuevo_id}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        conn.close()
