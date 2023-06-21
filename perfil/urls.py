from django.urls import path
from perfil import views


urlpatterns = [

    path('perfiles/', views.Perfil, name='perfil'),


    # path('usuarios/', views.ListadoUsuarios.as_view(), name='usuarios'),
    # path('eliminar_tareas/<int:pk>', EliminarTarea, name='eliminar_tareas'),
]
