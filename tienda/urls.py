from django.urls import path
from . import views

urlpatterns = [
    path("", views.tienda, name="tienda"),
    path("categoriaTienda/<int:categoria_id>/", views.categoriaTienda, name="categoriaTienda"),
]
