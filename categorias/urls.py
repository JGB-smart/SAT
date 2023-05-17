from django.urls import path
from categorias import views

urlpatterns = [

    path('lista_categorias/', views.ListadoCategorias.as_view(), name='lista_categorias'),
    path('agg_categorias/', views.AgregarCategoria.as_view(), name='agg_categorias'),
    path('eliminar_categoria/<int:pk>', views.EliminarCategoria, name='eliminar_categoria'),
    path('editar_categoria/<int:pk>', views.EditarCategoria.as_view(), name='editar_categoria')
    # path('usuarios/', views.ListadoUsuarios.as_view(), name='usuarios'),
]