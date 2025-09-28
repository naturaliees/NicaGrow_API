from fastapi import APIRouter
from modelos.estado_modelo import Estado

class EstadoAPI:
    def __init__(self):
        self.router = APIRouter()
        self.estados = [
            Estado(id=1, tipoEstado="Pendiente")
        ]
        self.router.get("/estados")(self.obtener_estados)
        self.router.post("/estados")(self.crear_estado)

    def obtener_estados(self):
        return self.estados

    def crear_estado(self, estado: Estado):
        self.estados.append(estado)
        return {"message": "Estado creado", "estado": estado}
