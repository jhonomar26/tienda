"""
URL configuration for ProyectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # El orden de los paths importa, wtf XD
    path("admin", admin.site.urls),
    # Nombre de la aplicacion, urls
    path("", include("gesProyectoWeb.urls")),
    path("servicios/", include("servicios.urls")),
    path("tienda/", include("tienda.urls")),
    path("carro/", include("carro.urls")),
    path("contacto/", include("contacto.urls")),
    path("blog/", include("blog.urls")),
    path("autenticacion/", include("autenticacion.urls")),
]
