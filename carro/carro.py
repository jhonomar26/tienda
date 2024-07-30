# El almacenamiento de datos, esta asociado a la sesión del usuario, es decir, que si se cierra la sesión el carrito de compras desaparecera
from tienda.models import Producto
import threading


class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        # Esto es para que cualquier acción que se realice sea eliminar, agregar, modificar, etc, se tenga en cuenta un bloqueo, para que otro usuarrio no haga alguna de estas acciones al mismo tiempo
        self.lock = threading.Lock()

        if not carro:
            carro = self.session["carro"] = {}
        self.carro = carro

    def agregar_producto(self, producto):
        with self.lock:
            if producto.cantidad > 0:
                producto_id_str = str(producto.id)
                if producto_id_str not in self.carro:
                    self.carro[producto_id_str] = {
                        "producto_id": producto.id,
                        "nombre": producto.nombre,
                        "precio": str(producto.precio),
                        "cantidad": 1,
                        "imagen": producto.imagen.url,
                    }
                else:
                    self.carro[producto_id_str]["cantidad"] += 1

                producto.cantidad -= 1
                if producto.cantidad == 0:
                    producto.disponibilidad = False
                producto.save()

                self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, producto):
        with self.lock:
            producto.id = str(producto.id)
            if producto.id in self.carro:
                del self.carro[producto.id]
                producto.disponibilidad = True
                producto.save()
                self.guardar_carro()

    def restar_producto(self, producto):
        # with self.lock:
        producto_id_str = str(producto.id)
        if producto_id_str in self.carro:
            self.carro[producto_id_str]["cantidad"] -= 1
            producto.cantidad += 1
            # Aqui se verfica si la cantidad de ese producto añadido al carrito es igual a cero, si es asi, lo eliminamos del carrito, aunque esto lo manejamos en el template en realidad
            if self.carro[producto_id_str]["cantidad"] == 0:
                self.eliminar(producto)
            else:
                producto.disponibilidad = True
                producto.save()
                self.guardar_carro()

    def limpiar_carro(self):
        with self.lock:

            for key, value in self.carro.items():
                try:
                    producto = Producto.objects.get(id=value["producto_id"])
                    producto.cantidad += value["cantidad"]
                    if producto.cantidad > 0:
                        producto.disponibilidad = True
                    producto.save()
                except Producto.DoesNotExist:
                    pass

            self.session["carro"] = {}
            self.session.modified = True
