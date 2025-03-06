from fastapi import APIRouter, HTTPException
from app.models .item import Item

#Inicializamos el ApiRouter
router = APIRouter()

#Creamos una BBDD temporal.
items_db = []

#Creamos un nuevo producto
#Utilizamos router para modularizar y organizar las rutas, responde_model=Item indica que que la respuesta será del tipo Item, lo que valida y serializa la salida.
@router.post("/items/", response_model = Item)
def new_product(item: Item):
    items_db.append(item)
    return item

#Obtenemos todos los productos
@router.get("/items/", response_model = list[Item])
def get_items():
    return items_db

#Obtener los productos por id.
@router.get("/items/{item_id}/", response_model = Item)
def get_item_by_id(item_id: int):
    for item in item_id:
        if item.id == item_id:
            return item
    raise HTTPException(status_code = 404, message = "Error, el id del producto no es válido")

#Eliminar un producto por id
def eliminar_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[index]
            return {"mensaje": "Item eliminado"}
    raise HTTPException(status_code=404, detail="Item no encontrado")