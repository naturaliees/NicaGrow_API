from fastapi import FastAPI
from entidades.cliente import ClienteAPI
from entidades.ciudad import CiudadAPI
from entidades.vendedor import VendedorAPI
from entidades.credenciales import CredencialAPI
from entidades.categoria import CategoriaAPI
from entidades.producto import ProductoAPI
from entidades.estado import EstadoAPI
from entidades.venta import VentaAPI
from entidades.metodopago import MetodoPagoAPI
from entidades.metodoenvio import MetodoEnvioAPI
from entidades.pedido import PedidoAPI
from entidades.detallpedido import DetallePedidoAPI
from entidades.historialbusqueda import HistorialBusquedaAPI
from entidades.resenia import ResenaAPI

app = FastAPI()

# registra routers
app.include_router(ClienteAPI().router)
app.include_router(CiudadAPI().router)
app.include_router(VendedorAPI().router)
app.include_router(CredencialAPI().router)
app.include_router(CategoriaAPI().router)
app.include_router(ProductoAPI().router)
app.include_router(EstadoAPI().router)
app.include_router(VentaAPI().router)
app.include_router(MetodoPagoAPI().router)
app.include_router(MetodoEnvioAPI().router)
app.include_router(PedidoAPI().router)
app.include_router(DetallePedidoAPI().router)
app.include_router(HistorialBusquedaAPI().router)
app.include_router(ResenaAPI().router)
