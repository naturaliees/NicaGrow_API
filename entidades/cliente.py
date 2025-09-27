from fastapi import APIRouter
from modelos.cliente_modelo import Cliente

class ClienteAPI:
    def __init__(self):
        self.router = APIRouter()
        self.clientes = [
            Cliente(id=1, nombre= "William", apellidos= "Graham", telefono="9900-5500", fnacimiento="1995-09-09",idCiudad='M')
        ]
        self.router.get("/clientes")(self.obtener_cliente)
        self.router.post("/clientes")(self.crear_cliente)

    def obtener_cliente(self):
        return self.clientes

    def crear_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        return {"message": "Cliente creado", "cliente": cliente}