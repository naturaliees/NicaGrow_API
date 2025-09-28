from pydantic import BaseModel
from typing import Optional

class Venta(BaseModel):
    id: Optional[int] = None
    idVendedor: int
    idProducto: int
    idEstado: int
    descripcion: str
    cantidad: int
