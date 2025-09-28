from pydantic import BaseModel
from typing import Optional

class MetodoEnvio(BaseModel):
    id: Optional[int] = None
    metodoEnvio: str
