from fastapi import APIRouter
from modelos.metodopago_modelo import MetodoPago

class MetodoPagoAPI:
    def __init__(self):
        self.router = APIRouter()
        self.metodos = [
            MetodoPago(id=1, metodo="Efectivo")
        ]
        self.router.get("/metodos_pago")(self.obtener_metodos)
        self.router.post("/metodos_pago")(self.crear_metodo)

    def obtener_metodos(self):
        return self.metodos

    def crear_metodo(self, metodo: MetodoPago):
        self.metodos.append(metodo)
        return {"message": "Metodo de pago creado", "metodo": metodo}
