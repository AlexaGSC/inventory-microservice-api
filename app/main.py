from fastapi import FastAPI
from app.routes import items

#Inicializamos la app.
app = FastAPI()

#Definimos la ruta en el endpoin raíz.
@app.get("/")
def read_root():
    return {"message": "¡Hola, Bienvenido a mi pequeña app!"} #Devuelve un mensaje JSON.

#Incluiremos las rutas de routes/items con la api principal
app.include_router(items.router)