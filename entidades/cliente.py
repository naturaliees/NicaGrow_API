from fastapi import APIRouter
from modelos.cliente_modelo import Cliente

class ClienteAPI:
    def __init__(self):
        self.router = APIRouter()
        self.cliente = [
            Cliente(idCliente=1, nombre= "William", apellidos= "Graham",
                    telefono="9900-5500", fnacimiento="09-09-1995   " ,idCiudad='M')

        ]
        self.router.get("/cliente")(self.obtener_cliente)
        self.router.post("/cliente")(self.crear_cliente)

def obtener_cliente(self):
    return self.cliente

def crear_cliente(self, cliente: Cliente):
    self.cliente.append(cliente)
    return {"message": "Cliente creado", "cliente": cliente}