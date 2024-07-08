from django.db import models


# Create your models here.
class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    # Al momento de subir una imagen, lo hace en una subcarpeta dentro de media llamada servicios
    imagen = models.ImageField(upload_to='servicios')
    # La fecha en la que se creo un servicio
    created = models.DateTimeField(auto_now_add=True)
    # La fecha en la que se actualizo
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def __str__(self):
        return self.titulo
