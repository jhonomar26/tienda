from django.shortcuts import render, HttpResponse
from servicios.models import Servicio


# Create your views here.
def home(request):
    return render(request, "gesProyectoWeb/home.html")
    # return HttpResponse("Home")




def tienda(request):
    return render(request, "gesProyectoWeb/tienda.html")





