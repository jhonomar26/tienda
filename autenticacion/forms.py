# registro/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            # Aplicación de bootrap a algunos elementos
            field.widget.attrs["class"] = "form-control  bg-transparent text-white"
            field.widget.attrs["placeholder"] = field.label
