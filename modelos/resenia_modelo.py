from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Resena(BaseModel):
    id: Optional[int] = None
    idCliente: int
    idProducto: int
    calificacion: int
    descripcion: Optional[str] = None
    fecha: datetime
