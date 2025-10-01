# NicaGrow
NicaGrow_API es el backend del proyecto NicaGrow, una aplicación diseñada para apoyar a los emprendedores locales de Nicaragua en la gestión de sus negocios. La API ofrece los servicios necesarios para el registro de usuarios, administración de productos, gestión de ventas y comunicación entre compradores y vendedores.

## Objetivos
Brindar a los emprendedores una herramienta tecnológica que:
* Facilite la publicación y promoción de productos.
* Permita gestionar clientes, pedidos y ventas.
* Ofrezca un historial de transacciones y reseñas de productos.
* Integre métodos de pago y opciones de envío.

## Estructura del proyecto
NicaGrowAPI/
│── entidades/              # Definición de las entidades principales del negocio
│   ├── categoria.py
│   ├── ciudad.py
│   ├── cliente.py
│   ├── credenciales.py
│   ├── detallepedido.py
│   ├── estado.py
│   ├── historialbusqueda.py
│   ├── metodoenvío.py
│   ├── metodopago.py
│   ├── pedido.py
│   ├── producto.py
│   ├── reseña.py
│   ├── vendedor.py
│   └── venta.py
│
│── modelos/                # Modelos de datos asociados a cada entidad
│   ├── categoria_modelo.py
│   ├── ciudad_modelo.py
│   ├── cliente_modelo.py
│   ├── credenciales_modelo.py
│   ├── detallepedido_modelo.py
│   ├── estado_modelo.py
│   ├── historialbusqueda_modelo.py
│   ├── metodoenvío_modelo.py
│   ├── metodopago_modelo.py
│   ├── pedido_modelo.py
│   ├── producto_modelo.py
│   ├── reseña_modelo.py
│   ├── vendedor_modelo.py
│   └── venta_modelo.py
│
│── main.py                 # Punto de entrada de la aplicación
│── README.md               # Documentación del proyecto

## Instalación y ejecución
1. Clonar el repositorio:
   * git clone https://github.com/naturaliees/NicaGrow_API.git
2. cd NicaGrow_API
3. Crear un entorno virtual e instalar dependencias:
   * python -m venv venv
   * source venv/bin/activate   # En Linux/Mac
   * venv\Scripts\activate      # En Windows
4. instalar dependencia
   * pip install fastapi uvicorn pydantic
5. Ejecutar el servidor
   * uvicorn main:app --reload
4. Ejecutar el proyecto:
   * python main.py
## Endpoints principales (version inicial)

| Método | Endpoint            | Descripción                        |
| ------ | ------------------- | ---------------------------------- |
| POST   | `/api/clientes`     | Registrar un nuevo cliente en el sistema  |
| GET    | `/api/clientes/{id}`| Obtener información de un cliente por su ID |
| POST   | `/api/vendedores`   | Registrar un nuevo vendedor     |
| GET   | `/api/vendedores/{id}`     | Consultar la información de un vendedor    |
| POST   | `/api/productos` | Publicar un nuevo producto     |
| GET   | `/api/productos` | Listar todos los productos disponibles    |


## Funcionalidades Principales
  * Gestión de usuarios: clientes, vendedores y credenciales.
  * Gestión de productos: creación, edición, publicación y reseñas.
  * Gestión de pedidos y ventas: detalle de pedidos, historial, estados.
  * Soporte de métodos de pago y envío.
  * Historial de búsqueda para mejorar experiencia del usuario.

## Tecnologías utilizadas
* Python 3.12.8
* FastAPI
* Uvicorn (Servidor ASGI)
