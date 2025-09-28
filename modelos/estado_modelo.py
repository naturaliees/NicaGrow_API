from pydantic import BaseModel
from typing import Optional

class Estado(BaseModel):
    id: Optional[int] = None
    tipoEstado: str
