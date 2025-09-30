from fastapi import APIRouter
from modelos.credenciales_modelo import Credencial

class CredencialAPI:
    def __init__(self):
        self.router = APIRouter()
        self.credenciales = [
            Credencial(id=1, correo="william@gmail.com", contrasena="contrasenia", codigoVerificacion="ABC123", idCliente=1, idVendedor=None)
        ]
        self.router.get("/credenciales")(self.obtener_credenciales)
        self.router.post("/credenciales")(self.crear_credencial)

    def obtener_credenciales(self):
        return self.credenciales

    def crear_credencial(self, credencial: Credencial):
        self.credenciales.append(credencial)
        return {"message": "Credencial creada", "credencial": credencial}
