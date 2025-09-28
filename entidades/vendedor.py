from fastapi import APIRouter
from modelos.vendedor_modelo import Vendedor

class VendedorAPI:
    def __init__(self):
        self.router = APIRouter()
        self.vendedores = [
            Vendedor(id=1, nombre="Ana", apellidos="Pérez", nombreNegocio="Tienda Ana", telefono="8888-2222", fnacimiento="1990-01-01", idCiudad='M')
        ]
        self.router.get("/vendedores")(self.obtener_vendedores)
        self.router.post("/vendedores")(self.crear_vendedor)

    def obtener_vendedores(self):
        return self.vendedores

    def crear_vendedor(self, vendedor: Vendedor):
        self.vendedores.append(vendedor)
        return {"message": "Vendedor creado", "vendedor": vendedor}
