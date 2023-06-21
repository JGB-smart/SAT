from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def Perfil(request):


    return render(request,'perfil.html')
