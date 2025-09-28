from pydantic import BaseModel
from typing import Optional

class DetallePedido(BaseModel):
    id: Optional[int] = None
    idPedido: int
    idProducto: int
    cantidad: int
