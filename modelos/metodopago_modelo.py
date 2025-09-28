from pydantic import BaseModel
from typing import Optional

class MetodoPago(BaseModel):
    id: Optional[int] = None
    metodo: str
