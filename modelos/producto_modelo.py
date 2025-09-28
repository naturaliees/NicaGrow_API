from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

class Producto(BaseModel):
    id: Optional[int] = None
    idVendedor: int
    nombreProducto: str
    foto: Optional[str] = None  # ruta/base64/URL — ajusta según cómo manejes imágenes
    precio: Decimal
    idCategoria: int
