from django.urls import path
from calificaciones import views



urlpatterns = [

        path('lista_calificacion/', views.ListadoCalificacion.as_view(), name='lista_calificacion'),

    # path('lista_tareas/', views.ListadoTareas.as_view(), name='lista_tareas'),
    #  path('usuarios/', views.Comentarios, name='usuarios'),
]