from django.urls import path
from usuarios import views


urlpatterns = [
    path('lista_usuarios/', views.ListadoUsuarios.as_view(), name='lista_usuarios'),
    path('lista_usuarios_grupos/', views.ListadoUsuario_Grupo.as_view(), name='lista_usuarios_grupos'),
    path('agregar_usuarios/', views.AgregarUsuario.as_view(), name='agregar_usuario'),
    
    # path('usuarios/', views.ListadoUsuarios.as_view(), name='usuarios'),
]
