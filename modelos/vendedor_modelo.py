from pydantic import BaseModel
from datetime import date
from typing import Optional

class Vendedor(BaseModel):
    id: Optional[int] = None
    nombre: str
    apellidos: str
    nombreNegocio: str
    telefono: str
    fnacimiento: date
    idCiudad: str
