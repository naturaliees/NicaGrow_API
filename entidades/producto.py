from fastapi import APIRouter
from modelos.producto_modelo import Producto
from decimal import Decimal

class ProductoAPI:
    def __init__(self):
        self.router = APIRouter()
        self.productos = [
            Producto(id=1, idVendedor=1, nombreProducto="Camiseta", foto=None, precio=Decimal("19.99"), idCategoria=1)
        ]
        self.router.get("/productos")(self.obtener_productos)
        self.router.post("/productos")(self.crear_producto)

    def obtener_productos(self):
        return self.productos

    def crear_producto(self, producto: Producto):
        self.productos.append(producto)
        return {"message": "Producto creado", "producto": producto}
