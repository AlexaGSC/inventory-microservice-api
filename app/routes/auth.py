from fastapi import APIRouter, HTTPException
from models.users import User

router = APIRouter()

test_user_db,= {
    "admin": "12345."
}

@router.post("/login/")
def login(user: User):
    #Verificamos si el username que el usuario ha ingresado, existe en nuestra bbdd falsa. Si el username existe en test_user_db, entonces buscamos su contraseña almacenada 
    if user.username in test_user_db and test_user_db[user.username] == user.password:
        return {"message": "Éxito en tu login"}

    raise HTTPException(status_code=401, detail="Credenciales incorrectas")