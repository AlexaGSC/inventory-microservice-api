from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel

router = APIRouter()

#Configuramos el contexto de hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Base de datos falsa (ahora con contraseñas hasheadas)
test_user_db = {
    "admin": pwd_context.hash("1234"),
    "user1": pwd_context.hash("abcd")
}

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login/")
def login(user: UserLogin):
    if user.username in test_user_db and pwd_context.verify(user.password, test_user_db[user.username]): #Usamos
        return {"message": "Login exitoso"}
    raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")
