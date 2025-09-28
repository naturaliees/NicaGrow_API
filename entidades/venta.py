from fastapi import APIRouter
from modelos.venta_modelo import Venta

class VentaAPI:
    def __init__(self):
        self.router = APIRouter()
        self.ventas = [
            Venta(id=1, idVendedor=1, idProducto=1, idEstado=1, descripcion="Venta inicial", cantidad=2)
        ]
        self.router.get("/ventas")(self.obtener_ventas)
        self.router.post("/ventas")(self.crear_venta)

    def obtener_ventas(self):
        return self.ventas

    def crear_venta(self, venta: Venta):
        self.ventas.append(venta)
        return {"message": "Venta creada", "venta": venta}
