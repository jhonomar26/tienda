from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    # La fecha en la que se creo
    created = models.DateTimeField(auto_now=True)
    # La fecha en la que se actualizo
    update = models.DateTimeField(auto_now=True)

    # Especificar el nombre en singular y en plural
    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    # Relacion de 1:n (para una categoria existen varios productos)
    categorias = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    contenido = models.CharField(max_length=50)
    # Al momento de subir una imagen, lo hace en una subcarpeta dentro de media llamada blog y con la segunda opcion que es opcional
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    # La fecha en la que se creo un producto
    # La fecha en la que se actualizo
    cantidad = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre
