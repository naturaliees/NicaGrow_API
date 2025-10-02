from fastapi import APIRouter, HTTPException
from modelos.vendedor_modelo import Vendedor

class VendedorAPI:
    def __init__(self):
        self.router = APIRouter()
        self.vendedores = [
            Vendedor(id=1, nombre="Ana", apellidos="Pérez", nombreNegocio="Tienda Ana", telefono="8888-2222", fnacimiento="1990-01-01", idCiudad='M')
        ]
        self.router.get("/vendedores")(self.obtener_vendedores)
        self.router.post("/vendedores")(self.crear_vendedor)
        self.router.put("/vendedores/{vendedor_id}")(self.actualizar_vendedor)
        self.router.delete("/vendedores/{vendedor_id}")(self.eliminar_vendedor)

    def obtener_vendedores(self):
        return self.vendedores

    def crear_vendedor(self, vendedor: Vendedor):
        self.vendedores.append(vendedor)
        return {"message": "Vendedor creado", "vendedor": vendedor}

    def actualizar_vendedor(self, vendedor_id: int, vendedor_actualizado: Vendedor):
        for i, vendedor in enumerate(self.vendedores):
            if vendedor.id == vendedor_id:
                self.vendedores[i] = vendedor_actualizado
                return {"message": "Vendedor actualizado", "vendedor": vendedor_actualizado}
            raise HTTPException(status_code=404, detail="Vendedor no encontrado")

    def eliminar_vendedor(self, vendedor_id: int):
        for i, vendedor in enumerate(self.vendedores):
            if vendedor.id == vendedor_id:
                eliminado = self.vendedores.pop(i)
                return {"message": "Vendedor eliminado", "vendedor": eliminado}
            raise HTTPException(status_code=404, detail="Vendedor no encontrado")