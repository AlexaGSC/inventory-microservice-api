from fastapi import APIRouter, HTTPException
from passlib.context import CryptContext
from app.models.users import UserLogin, test_user_db, pwd_context

router = APIRouter()

#Configuramos el contexto de hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

#Base de datos falsa (ahora con contraseñas hasheadas)
test_user_db = {
    "admin": pwd_context.hash("1234"),
    "user1": pwd_context.hash("abcd")
}

@router.post("/login/")
def login(user: UserLogin):
    #Verificamos si el username que el usuario ha ingresado, existe en nuestra bbdd falsa. Si el username existe en test_user_db, entonces buscamos su contraseña almacenada
    if user.username in test_user_db:
        hashed_password = test_user_db[user.username]  # Obtenemos la contraseña hasheada almacenada
        print(f"Usuario: {user.username}, Contraseña ingresada: {user.password}, Hash guardado: {hashed_password}")  # DEBUG

        if pwd_context.verify(user.password, hashed_password):  # Comparamos la ingresada con la hasheada
            return {"message": "Login exitoso"}
    
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")