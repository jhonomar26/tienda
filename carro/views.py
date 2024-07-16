from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import Producto, CategoriaProducto
from tienda.views import categoriaTienda

# Create your views here.


def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar_producto(producto)

    return redirect("tienda")


def agregar_producto_categoria(request, producto_id, categoriaId):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar_producto(producto)
    # categoriaTienda(request, categoriaId)
    return redirect("categoriaTienda", categoria_id=categoriaId)


def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto)
    return redirect("tienda")


def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto)
    return redirect("tienda")


def limpiar_carro(request):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect("tienda")
