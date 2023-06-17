from django.urls import path
from comentarios import views


urlpatterns = [


    path('tarea_comentario/', views.ListadoTareas.as_view(), name='tarea_comentario'),
    path('lista_comentarios/<int:pk>', views.comentarios, name='lista_comentarios'),

    # path('lista_tareas/', views.ListadoTareas.as_view(), name='lista_tareas'),
    #  path('usuarios/', views.Comentarios, name='usuarios'),
]