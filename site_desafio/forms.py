from dataclasses import fields
from django import forms
from .models import Autor
from .models import Editora
from .models import Livro


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        exclude = ()


class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        exclude = ()
        

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        exclude = ()