from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from perfil.models import Perfil

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class EditPerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['image','telf']

class EditPuestoForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['image','telf','puesto']        