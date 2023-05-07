from django.shortcuts import render, redirect
from django.contrib.auth import logout

def salir(request):
    logout(request)
    return redirect('/accounts/login')
