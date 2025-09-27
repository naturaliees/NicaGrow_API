from pydantic import BaseModel
from datetime import date
from typing import Optional

class Cliente(BaseModel):
    id: Optional[int] = None
    nombre: str
    apellidos: str
    telefono: str
    fnacimiento: date
    idCiudad: str