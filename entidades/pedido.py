from fastapi import APIRouter
from modelos.pedido_modelo import Pedido
from datetime import datetime
from decimal import Decimal

class PedidoAPI:
    def __init__(self):
        self.router = APIRouter()
        self.pedidos = [
            Pedido(id=1, idCliente=1, fechaPedido=datetime.now(), total=Decimal("39.98"), idMetodoPago=1, idMetodoEnvio=1, idEstado=1)
        ]
        self.router.get("/pedidos")(self.obtener_pedidos)
        self.router.post("/pedidos")(self.crear_pedido)

    def obtener_pedidos(self):
        return self.pedidos

    def crear_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)
        return {"message": "Pedido creado", "pedido": pedido}
