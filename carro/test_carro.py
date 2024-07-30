import sys
import os
import django
from django.test import RequestFactory

# Agrega la ruta del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProyectoWeb.settings")

# Configura Django
django.setup()

# Importa el modelo Producto y la clase Carro después de configurar Django
from tienda.models import Producto
from carro import Carro

# Crea una fábrica de solicitudes
factory = RequestFactory()

# Simula una solicitud de usuario
request = factory.get("/")

# Crea un producto de prueba
producto = Producto.objects.create(
    nombre="Producto de prueba",
    categorias_id=1,  # Asume que tienes una categoría con ID 1
    contenido="Descripción del producto de prueba",
    precio=10.0,
    cantidad=10,
)

# Inicializa el carrito
carro = Carro(request)

# Agrega el producto al carrito
carro.agregar(producto)
print("Carro después de agregar el producto:", request.session["carro"])
print("Numero total de productos: ", producto.cantidad)

# Resta el producto del carrito
carro.restar_producto(producto)
print("Carro después de restar el producto:", request.session["carro"])
print("Numero total de productos: ", producto.cantidad)
# Limpia el carrito

carro.limpiar_carro()
print("Carro después de limpiar:", request.session["carro"])
print("Numero total de productos: ", producto.cantidad)
