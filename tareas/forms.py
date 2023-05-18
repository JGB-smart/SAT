from django import forms
from .models import Tareas,Status,Prioridad,Categorias
from django.contrib.auth.models import User



# class TareasForm(forms.Form):
#     tarea = forms.TextInput(label="Nombre")
#     descripcion = forms.TextInput(label="Descripción")
#     categoria_id = forms.ModelChoiceField(label="Categoria",queryset=Categorias.objects.all())
#     prioridad_id = forms.ModelChoiceField(label="Prioridad",queryset=Prioridad.objects.all())
#     status_id = forms.ModelChoiceField(label="Status",queryset=Status.objects.all())
#     porcentaje = forms.NumberInput(label="Porcentaje")
#     Asignada_id = forms.ModelChoiceField(label="Asignar",queryset=User.objects.all())
#     CreadaPor_id = forms.ModelChoiceField(label="Creada por",queryset=User.objects.all())
#     Ffinal = forms.DateField(label="Fecha Final")