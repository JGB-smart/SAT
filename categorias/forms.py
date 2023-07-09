from django import forms
from categorias.models import Categorias

class CategoriasForm(forms.ModelForm):

    class Meta:
        model = Categorias
        fields = ['categoria']