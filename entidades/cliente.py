from fastapi import APIRouter, HTTPException
from modelos.cliente_modelo import Cliente

class ClienteAPI:
    def __init__(self):
        self.router = APIRouter()
        self.clientes = [
            Cliente(id=1, nombre= "William", apellidos= "Graham", telefono="9900-5500", fnacimiento="1995-09-09",idCiudad='M')
        ]
        self.router.get("/clientes")(self.obtener_cliente)
        self.router.post("/clientes")(self.crear_cliente)
        self.router.put("/clientes/{cliente_id}")(self.actualizar_cliente)
        self.router.delete("/clientes/{cliente_id}")(self.eliminar_cliente)

    def obtener_cliente(self):
        return self.clientes

    def crear_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        return {"message": "Cliente creado", "cliente": cliente}

    def actualizar_cliente(self, cliente_id: int, cliente_actualizado: Cliente):
        for i, cliente in enumerate(self.clientes):
            if cliente.id == cliente_id:
                self.clientes[i] = cliente_actualizado
                return {"message": "Cliente actualizado", "cliente": cliente_actualizado}
            raise HTTPException(status_code=404, detail="Cliente no encontrado")

    def eliminar_cliente(self, cliente_id: int):
        for i, cliente in enumerate(self.clientes):
            if cliente.id == cliente_id:
                eliminado = self.clientes.pop(i)
                return {"message": "Cliente eliminado", "cliente": eliminado}
            raise HTTPException(status_code=404, detail="Cliente no encontrado")