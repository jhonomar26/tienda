from django.urls import path
from . import views

# Cada vez que necesite utilizar una de las urls, solo tengo que escribir carro.nombreUrl
app_name = "carro"
urlpatterns = [
    path("agregar/<int:producto_id>/", views.agregar_producto, name="agregarProducto"),
    path('agregar/<int:producto_id>/<int:categoriaId>/', views.agregar_producto_categoria, name='agregarProductoCategoria'),
    path(
        "eliminar/<int:producto_id>/", views.eliminar_producto, name="eliminarProducto"
    ),
    path("restar/<int:producto_id>/", views.restar_producto, name="restarProducto"),
    path("limpiar/", views.limpiar_carro, name="limpiarCarro"),
]
