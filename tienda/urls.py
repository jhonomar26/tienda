from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(views.tienda), name="tienda"),
    path(
        "categoriaTienda/<int:categoria_id>/",
        login_required(views.categoriaTienda),
        name="categoriaTienda",
    ),
]
