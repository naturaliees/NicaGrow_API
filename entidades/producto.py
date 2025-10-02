from fastapi import APIRouter, HTTPException
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
        self.router.put("/productos/{producto_id}")(self.actualizar_producto)
        self.router.delete("/productos/{producto_id}")(self.eliminar_producto)

    def obtener_productos(self):
        return self.productos

    def crear_producto(self, producto: Producto):
        self.productos.append(producto)
        return {"message": "Producto creado", "producto": producto}

    def actualizar_producto(self, producto_id: int, producto_actualizado: Producto):
        for i, producto in enumerate(self.productos):
            if producto.id == producto_id:
                self.productos[i] = producto_actualizado
                return {"message": "Producto actualizado", "vendedor": producto_actualizado}
            raise HTTPException(status_code=404, detail="Producto no encontrado")

    def eliminar_producto(self, producto_id: int):
        for i, producto in enumerate(self.productos):
            if producto.id == producto_id:
                eliminado = self.productos.pop(i)
                return {"message": "Producto eliminado", "producto": eliminado}
            raise HTTPException(status_code=404, detail="Producto no encontrado")