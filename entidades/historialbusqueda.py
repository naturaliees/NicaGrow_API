from fastapi import APIRouter
from modelos.historialbusqueda_modelo import HistorialBusqueda
from datetime import datetime

class HistorialBusquedaAPI:
    def __init__(self):
        self.router = APIRouter()
        self.historial = [
            HistorialBusqueda(id=1, idCliente=1, busqueda="camiseta roja", fechaBusqueda=datetime.now())
        ]
        self.router.get("/historial_busqueda")(self.obtener_historial)
        self.router.post("/historial_busqueda")(self.crear_historial)

    def obtener_historial(self):
        return self.historial

    def crear_historial(self, item: HistorialBusqueda):
        self.historial.append(item)
        return {"message": "Busqueda registrada", "historial": item}
