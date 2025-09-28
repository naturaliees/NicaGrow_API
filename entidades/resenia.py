from fastapi import APIRouter
from modelos.resenia_modelo import Resena
from datetime import datetime

class ResenaAPI:
    def __init__(self):
        self.router = APIRouter()
        self.resenas = [
            Resena(id=1, idCliente=1, idProducto=1, calificacion=5, descripcion="Excelente producto", fecha=datetime.now())
        ]
        self.router.get("/resenas")(self.obtener_resenas)
        self.router.post("/resenas")(self.crear_resena)

    def obtener_resenas(self):
        return self.resenas

    def crear_resena(self, resena: Resena):
        self.resenas.append(resena)
        return {"message": "Reseña creada", "resena": resena}
