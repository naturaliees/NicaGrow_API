from fastapi import APIRouter
from modelos.detallepedido_modelo import DetallePedido

class DetallePedidoAPI:
    def __init__(self):
        self.router = APIRouter()
        self.detalles = [
            DetallePedido(id=1, idPedido=1, idProducto=1, cantidad=2)
        ]
        self.router.get("/detalles_pedido")(self.obtener_detalles)
        self.router.post("/detalles_pedido")(self.crear_detalle)

    def obtener_detalles(self):
        return self.detalles

    def crear_detalle(self, detalle: DetallePedido):
        self.detalles.append(detalle)
        return {"message": "Detalle de pedido creado", "detalle": detalle}
