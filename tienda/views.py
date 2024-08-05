from django.shortcuts import render
from tienda.models import Producto, CategoriaProducto
from django.contrib.auth.decorators import login_required

# Create your views here.

# Create your views here.


def tienda(request):
    productos = Producto.objects.all()
    categorias = CategoriaProducto.objects.all()

    return render(
        request,
        "tienda/tienda.html",
        {
            "productos": productos,
            "categorias": categorias,
        },
    )


def categoriaTienda(request, categoria_id):
    categoria = CategoriaProducto.objects.get(id=categoria_id)
    productos = Producto.objects.filter(categorias=categoria)

    return render(
        request,
        "tienda/categoria.html",
        {
            "categorias": CategoriaProducto.objects.all(),
            "productos": productos,
            "categoriaId": categoria_id,
        },
    )
