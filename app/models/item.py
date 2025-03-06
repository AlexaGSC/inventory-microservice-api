from pydantic import BaseModel

#Crearemos la clase Item que heredará los atributos de BaseModel
class Item(BaseModel):
    id: int
    nombre: str
    precio: float
    stock: int