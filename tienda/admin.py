from django.contrib import admin
from .models import Producto, CategoriaProducto


# Register your models here.
class categoriaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "update")


class productoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "update")


admin.site.register(CategoriaProducto, categoriaAdmin)
admin.site.register(Producto, productoAdmin)
