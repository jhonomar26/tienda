from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from tienda.models import Producto


class Carro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto, through="ItemCarro")
    creado_en = models.DateTimeField(auto_now_add=True)
    modificado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Carro de {self.user.username}"
class ItemCarro(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en {self.carro}"
