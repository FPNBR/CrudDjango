from django import forms
from .models import Autor
from .models import Editora


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        exclude = ()


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        exclude = ()

