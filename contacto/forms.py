from django import forms
from django.utils.translation import gettext_lazy as _


class formularioContacto(forms.Form):
    nombre = forms.CharField(
        label=_("Nombre"),
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control bg-transparent text-white "}),
    )
    email = forms.EmailField(
        label=_("Correo electrónico"),
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control  bg-transparent text-white"}),
    )
    contenido = forms.CharField(
        label=_("Contenido"),
        required=True,
        widget=forms.Textarea(attrs={"class": "form-control bg-transparent text-white ", "rows": 5}),
    )
