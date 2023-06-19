from django.urls import path
from tareas.views import (ListadoTareas,
CrearTarea,
EliminarTarea,
EditarTarea,
CalificarTarea,
ListadoArchivoTareas)

urlpatterns = [

    path('lista_tareas/', ListadoTareas.as_view(), name='lista_tareas'),
    path('agg_tareas/', CrearTarea.as_view(), name='agg_tareas'),
    path('eliminar_tareas/<int:pk>', EliminarTarea, name='eliminar_tareas'),
    path('editar_tareas/<int:pk>', EditarTarea, name='editar_tareas'),
    path('calificar_tarea/', CalificarTarea.as_view(), name='calificar_tarea'),
    path('lista_archivo/', ListadoArchivoTareas.as_view(), name='lista_archivo'),


    # path('usuarios/', views.ListadoUsuarios.as_view(), name='usuarios'),
]