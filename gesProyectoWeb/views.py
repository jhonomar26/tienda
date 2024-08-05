from django.shortcuts import render, HttpResponse
from servicios.models import Servicio
from carro.carro import Carro


# Create your views here.
def home(request):
    carro = Carro(request)
    return render(request, "gesProyectoWeb/home.html")
    # return HttpResponse("Home")


def tienda(request):
    return render(request, "gesProyectoWeb/tienda.html")
