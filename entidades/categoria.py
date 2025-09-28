from fastapi import APIRouter
from modelos.categoria_modelo import Categoria

class CategoriaAPI:
    def __init__(self):
        self.router = APIRouter()
        self.categorias = [
            Categoria(id=1, categoria="Ropa")
        ]
        self.router.get("/categorias")(self.obtener_categorias)
        self.router.post("/categorias")(self.crear_categoria)

    def obtener_categorias(self):
        return self.categorias

    def crear_categoria(self, categoria: Categoria):
        self.categorias.append(categoria)
        return {"message": "Categoria creada", "categoria": categoria}
