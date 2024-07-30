from django.shortcuts import render, redirect
from django.views.generic import View
from django.shortcuts import render
from django.views.generic import View
from .forms import CustomUserCreationForm, formularioRegistro
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from carro.views import limpiar_carro

# from django.contrib.auth.forms import AuthenticationForm


# Create your views here.


class VRegistro(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, "registro/registro.html", {"form": form})

    def post(self, request):
        # Traemos la información del formulario atraves del request, solo tenemos usuario y contraseña
        form = CustomUserCreationForm(request.POST)
        # Se almacena en la base de datos
        if form.is_valid():
            usuario = form.save()
            # Inicia sesión con el usuario registrado
            login(request, usuario)
            return redirect("home")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, "registro/registro.html", {"form": form})


def cerrar_sesion(request):
    # Damos por hecho que cuando se limpia el carro, estamos cerrando sesión
    #!Nota importante: Sabemos que no hay persistencia con los datos del carro, por tanto, tenemos que si o si,
    # !los productos que se almacenen en el carro la cantidad se regrese a cada uno de estos, ademas,
    # !que si ya estan disponibles, el usuario pueda añadirlos a su carrito de compras
    return redirect("carro:limpiarCarro")


def logear(request):
    if request.method == "POST":
        form = formularioRegistro(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=contra)
            if usuario is not None:
                login(request, usuario)
                return redirect("home")
            else:
                messages.error(request, "Usuario no válido")
                print("Usuario no valido")
                return render(request, "login/login.html", {"form": form})

        else:
            messages.error(request, "Información incorrecta")
            print("Información incorrecta")
            return render(request, "login/login.html", {"form": form})

    form = formularioRegistro()
    return render(request, "login/login.html", {"form": form})
