from django.urls import path
from categorias import views

urlpatterns = [

    path('lista_categorias/', views.ListadoCategorias.as_view(), name='lista_categorias'),
    # path('usuarios/', views.ListadoUsuarios.as_view(), name='usuarios'),
]