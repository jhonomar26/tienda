from django.shortcuts import render, redirect
from django.views.generic import View
from django.shortcuts import render
from django.views.generic import View
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages


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
    logout(request)
    return redirect("home")
