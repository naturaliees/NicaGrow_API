from fastapi import APIRouter, HTTPException
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

    def actualizar_pedido(self, pedido_id: int, pedido_actualizado: Pedido):
        for i, pedido in enumerate(self.pedidos):
            if pedido.id == pedido_id:
                self.pedidos[i] = pedido_actualizado
                return {"message": "Pedido actualizado", "pedido": pedido_actualizado}
            raise HTTPException(status_code=404, detail="Pedido no encontrado")

    def eliminar_pedido(self, pedido_id: int):
        for i, pedido in enumerate(self.pedidos):
            if pedido.id == pedido_id:
                eliminado = self.pedidos.pop(i)
                return {"message": "Pedido eliminado", "pedido": eliminado}
            raise HTTPException(status_code=404, detail="Pedido no encontrado")
