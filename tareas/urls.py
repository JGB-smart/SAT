from django.urls import path
from tareas import views

urlpatterns = [

    path('lista_tareas/', views.ListadoTareas.as_view(), name='lista_tareas'),
    # path('usuarios/', views.ListadoUsuarios.as_view(), name='usuarios'),
]