from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path("", login_required(views.blog), name="blog"),
    path("categoria/<int:categoria_id>/", login_required(views.categoria), name="categoria"),
]
