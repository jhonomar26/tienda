from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    # La fecha en la que se creo
    created = models.DateTimeField(auto_now_add=True)
    # La fecha en la que se actualizo
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    # Al momento de subir una imagen, lo hace en una subcarpeta dentro de media llamada blog y con la segunda opcion que es opcional
    imagen = models.ImageField(upload_to="blog", blank=True)
    # Cuando se borre un usuario se elmiminen tambien sus pots
    # Relacion de 1:n (para un autor existen varios posts)
    categorias = models.ManyToManyField(Categoria)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    # La fecha en la que se creo un servicio
    created = models.DateTimeField(auto_now_add=True)
    # La fecha en la que se actualizo
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.titulo
