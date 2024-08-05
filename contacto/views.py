from django.shortcuts import render, redirect
from .forms import formularioContacto
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.decorators import login_required

import logging

# Create your views here.

logger = logging.getLogger(__name__)


def contacto(request):
    formulario_contacto = formularioContacto()
    if request.method == "POST":
        # Cargar en nuestro formulario, la informacion que hay en request
        formulario_contacto = formularioContacto(data=request.POST)

        if formulario_contacto.is_valid():

            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            contenido = request.POST.get("contenido")
            try:
                send_mail(
                    "Aplicacion correos",
                    "El usuario con nombre {} con la dirección {}, escribe lo siguiente:\n\n {}".format(
                        nombre,
                        email,
                        contenido,
                    ),
                    email,
                    ["apuntesjhonomar@gmail.com"],
                    fail_silently=False,
                )

                return redirect("/contacto/?valido")
            except Exception as e:
                # Imprimir el error en la consola
                print(f"ERROR: {e}")
                # O usar el logger configurado para registrar el error
                logger.error(f"Error al enviar el correo: {e}")
                return redirect("/contacto/?novalido")
    else:
        return render(
            request, "contacto/contacto.html", {"miFormulario": formulario_contacto}
        )
