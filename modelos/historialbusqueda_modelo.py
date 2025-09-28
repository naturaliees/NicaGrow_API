from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class HistorialBusqueda(BaseModel):
    id: Optional[int] = None
    idCliente: int
    busqueda: str
    fechaBusqueda: datetime
