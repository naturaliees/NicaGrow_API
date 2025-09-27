from fastapi import FastAPI

from entidades import cliente
from entidades.cliente import ClienteAPI

app = FastAPI()

app.include_router(ClienteAPI().router)