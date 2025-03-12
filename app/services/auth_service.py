import os
import jwt
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from fastapi import HTTPException

# Cargar las variables del archivo .env
load_dotenv()

# Leer la clave secreta desde .env
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"  # Definir el algoritmo de cifrado

# Función para generar un token JWT
def create_jwt_token(username: str):
    """
    Genera un token JWT con un tiempo de expiración de 1 hora.
    """
    payload = {
        "sub": username,  # Usuario
        "exp": datetime.now(timezone.utc) + timedelta(hours=1)  # Expira en 1 hora
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

# Función para verificar y decodificar un token
def verify_jwt_token(token: str):
    """
    Verifica y decodifica un token JWT.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Si es válido, devuelve los datos del token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expirado")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Token inválido")
