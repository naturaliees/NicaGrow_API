from fastapi import APIRouter
from modelos.ciudad_modelo import Ciudad

class CiudadAPI:
    def __init__(self):
        self.router = APIRouter()
        self.ciudades = [
            Ciudad(id='M', ciudad='Managua')
        ]
        self.router.get("/ciudades")(self.obtener_ciudades)
        self.router.post("/ciudades")(self.crear_ciudad)

    def obtener_ciudades(self):
        return self.ciudades

    def crear_ciudad(self, ciudad: Ciudad):
        self.ciudades.append(ciudad)
        return {"message": "Ciudad creada", "ciudad": ciudad}
