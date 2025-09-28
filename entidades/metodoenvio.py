from fastapi import APIRouter
from modelos.metodoenvio_modelo import MetodoEnvio

class MetodoEnvioAPI:
    def __init__(self):
        self.router = APIRouter()
        self.metodos_envio = [
            MetodoEnvio(id=1, metodoEnvio="Domicilio")
        ]
        self.router.get("/metodos_envio")(self.obtener_metodos_envio)
        self.router.post("/metodos_envio")(self.crear_metodo_envio)

    def obtener_metodos_envio(self):
        return self.metodos_envio

    def crear_metodo_envio(self, metodo: MetodoEnvio):
        self.metodos_envio.append(metodo)
        return {"message": "Metodo de envío creado", "metodo": metodo}
