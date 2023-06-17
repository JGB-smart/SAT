from django import forms
from .models import Comentarios
from tareas.models import Tareas
from django.contrib.auth.models import User



class ComentariosForm(forms.ModelForm):
    
    class Meta:
        model = Comentarios
        fields = '__all__'

    comentario = forms.CharField(label="Comentar",widget=forms.Textarea(attrs={'class': 'form-control','id': 'textAreaExample','rows': '4'}))
    tarea = forms.ModelChoiceField(label=False,queryset=Tareas.objects.all(),disabled = True, required = False,widget=forms.Select(attrs={'class': 'form-control','hidden' : True})) 
    user = forms.ModelChoiceField(label=False,queryset=User.objects.all(),disabled = True, required = False,widget=forms.Select(attrs={'class': 'form-control','hidden' : True}))

