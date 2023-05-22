from django.urls import path
from tareas import views

urlpatterns = [

    path('lista_tareas/', views.ListadoTareas.as_view(), name='lista_tareas'),
    path('agg_tareas/', views.CrearTarea.as_view(), name='agg_tareas'),
    path('eliminar_tareas/<int:pk>', views.EliminarTarea, name='eliminar_tareas'),
    path('editar_tareas/<int:pk>', views.EditarTarea, name='editar_tareas'),
    # path('usuarios/', views.ListadoUsuarios.as_view(), name='usuarios'),
]