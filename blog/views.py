from django.shortcuts import render
from blog.models import Post, Categoria

# Create your views here.


def blog(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "blog/blog.html", {"posts": posts, "categorias": categorias})


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    print(categoria_id)
    posts = Post.objects.filter(categorias=categoria)

    return render(
        request,
        "blog/categoria.html",
        {
            "categorias": Categoria.objects.all(),
            "posts": posts,
        },
    )
