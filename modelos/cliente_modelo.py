from pydantic import BaseModel
from datetime import date

class Cliente(BaseModel):
    idCliente: int
    nombre: str
    apellidos: str
    telefono: str
    fnacimiento: date
    idCiudad: chr