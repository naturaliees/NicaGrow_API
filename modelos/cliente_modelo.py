from pydantic import BaseModel
from datetime import date

class Cliente(BaseModel):
    nombre: str
    apellidos: str
    telefono: str
    fnacimiento: date
    idciudad: int