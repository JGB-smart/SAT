from django.urls import path
from usuarios import views


urlpatterns = [
    path('lista_usuarios/', views.Usuarios, name='lista_usuarios'),
    # path('usuarios/', views.ListadoUsuarios.as_view(), name='usuarios'),
]
