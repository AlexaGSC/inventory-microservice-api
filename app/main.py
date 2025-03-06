from fastapi import FastAPI
from app.routes import items, auth

#Inicializamos la app.
app = FastAPI()

#Definimos la ruta en el endpoin raíz.
@app.get("/")
def read_root():
    return {"message": "¡Hola, Bienvenido a mi pequeña app!"} #Devuelve un mensaje JSON.

#Incluiremos las rutas de routes/items con la api principal, al igual que haremos con las siguientes rutas.
app.include_router(items.router)

app.include_router(auth.router)