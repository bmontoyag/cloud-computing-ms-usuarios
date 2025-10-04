from fastapi import Header, HTTPException
from jose import jwt

def validar_token(Authorization: str = Header(None)):
    if not Authorization:
        raise HTTPException(status_code=401, detail="Token no proporcionado")
    token = Authorization.replace("Bearer ", "")
    try:
        decoded = jwt.get_unverified_claims(token)
        return decoded
    except Exception:
        raise HTTPException(status_code=401, detail="Token inválido")
