# Importa el módulo 'admin' de Django para registrar modelos en el panel de administración.
from django.contrib import admin

# Importa los modelos Categoria y Post desde el archivo models.py del mismo directorio.
from .models import Categoria, Post

# Define una clase 'categoriaAdmin' que personaliza la visualización del modelo Categoria en el panel de administración.
class categoriaAdmin(admin.ModelAdmin):
    # Define los campos que se mostrarán como de solo lectura en el panel de administración.
    readonly_fields=('created','update')

# Define una clase 'PostAdmin' que personaliza la visualización del modelo Post en el panel de administración.
class PostAdmin(admin.ModelAdmin):
    # Define los campos que se mostrarán como de solo lectura en el panel de administración.
    readonly_fields=('created','update')

# Registra el modelo Categoria en el panel de administración, utilizando la clase 'categoriaAdmin' para personalizar su visualización.
admin.site.register(Categoria, categoriaAdmin)

# Registra el modelo Post en el panel de administración, utilizando la clase 'PostAdmin' para personalizar su visualización.
admin.site.register(Post, PostAdmin)
