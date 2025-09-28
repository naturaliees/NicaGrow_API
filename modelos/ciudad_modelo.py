# modelos/ciudad_modelo.py
from pydantic import BaseModel
from typing import Optional

class Ciudad(BaseModel):
    id: Optional[str] = None
    ciudad: str
