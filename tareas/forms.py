from django import forms
from .models import Tareas
from .models import Status
from django.db.models import Q
from django.contrib.auth.models import User




class TareasForm(forms.ModelForm):

    class Meta:
        model = Tareas
        fields =  '__all__'
        exclude = ['Fterminada']


    status = forms.ModelChoiceField(label="Status",queryset= Status.objects.all(),required = True,widget=forms.Select(attrs={'class': 'form-control'}))
    Ffinal = forms.DateField(label="Fecha Final",widget=forms.DateInput(attrs={'class': 'form-control','placeholder' : '20/5/2023'}))
    CreadaPor = forms.ModelChoiceField(label=False,queryset=User.objects.all(),disabled = True, required = False,widget=forms.Select(attrs={'class': 'form-control','hidden' : True}))
    user = forms.ModelChoiceField(label="Asignar",queryset=User.objects.all())



    # tarea = forms.CharField(required=True, widget=forms.TextInput())
    # descripcion = forms.CharField(required=True, widget=forms.TextInput())
    # categoria_id = forms.ModelChoiceField(label='categoria',queryset=Categorias.objects.all())
    # prioridad_id = forms.ModelChoiceField(label='prioridad',queryset=Prioridad.objects.all())
    # status_id = forms.ModelChoiceField(label='status', queryset=Status.objects.all())
    # porcentaje = forms.IntegerField(widget=forms.NumberInput())
    # Asignada_id = forms.ModelChoiceField(label="Asignar",queryset=User.objects.all())
    # CreadaPor_id = forms.ModelChoiceField(label="Creada por",queryset=User.objects.all())
    # Ffinal = forms.DateField(label="Fecha Final")

class TareasForm2(forms.ModelForm):

    class Meta:
        model = Tareas
        fields =  '__all__'
        exclude = ['Fterminada']


    status = forms.ModelChoiceField(label="Status",queryset= Status.objects.all().exclude(status = 'Re_abierta').exclude(status = 'Revisión').exclude(status='Finalizada'),required = False,widget=forms.Select(attrs={'class': 'form-control'}))
    Ffinal = forms.DateField(label="Fecha Final",widget=forms.DateInput(attrs={'class': 'form-control','placeholder' : '20/5/2023'}))
    CreadaPor = forms.ModelChoiceField(label=False,queryset=User.objects.all(),disabled = True, required = False,widget=forms.Select(attrs={'class': 'form-control','hidden' : True}))
    user = forms.ModelChoiceField(label=False,queryset=User.objects.all(),disabled = True, required = False,widget=forms.Select(attrs={'class': 'form-control','hidden' : True}))