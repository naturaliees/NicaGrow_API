from pydantic import BaseModel
from typing import Optional

class Credencial(BaseModel):
    id: Optional[int] = None
    correo: str
    contrasena: str
    codigoVerificacion: str
    idCliente: Optional[int] = None
    idVendedor: Optional[int] = None
