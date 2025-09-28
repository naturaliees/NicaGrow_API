from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from decimal import Decimal

class Pedido(BaseModel):
    id: Optional[int] = None
    idCliente: int
    fechaPedido: datetime
    total: Decimal
    idMetodoPago: int
    idMetodoEnvio: int
    idEstado: int
