from pydantic import BaseModel
import datetime

#Creamos la clase para User, también heredará los atributos de BaseModel.
class User(BaseModel):
    username: str
    password: str
