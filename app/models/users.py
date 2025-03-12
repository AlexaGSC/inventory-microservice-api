from pydantic import BaseModel
from passlib.context import CryptContext

# Configurar el contexto de hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Base de datos falsa con contraseñas encriptadas
test_user_db = {
    "admin": pwd_context.hash("1234"),  # Contraseña "1234" encriptada
    "user1": pwd_context.hash("abcd")   # Contraseña "abcd" encriptada
}

# Modelo para el login del usuario
class UserLogin(BaseModel):
    username: str
    password: str
