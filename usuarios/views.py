from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DeleteView

from django.contrib.auth.models import User
from perfil.models import Perfil

class ListadoUsuarios(ListView):
    model = User
    template_name = 'lista_usuarios.html'
    context_object_name = 'usuarios'             # permite cambiar de nombre al objetos listview que se llamara en la vista
    queryset=  User.objects.all()           #  Permite realizar filtros a la consulta
    
    @method_decorator(login_required)             #Puede agrupar decoradores
    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('productos.view_productos'):
        #       messages.success(request,"ACCESO DENEGADO")
        #       return redirect('home')
        #print(Perfil.objects.select_related('user').query)
        #print(User.objects.prefetch_related('username').query)
        # print(Group.users.all())

        return super( ListadoUsuarios,self).dispatch(request, *args, **kwargs)
    

    
class ListadoUsuario_Grupo(ListView):
    model = User
    template_name = 'lista_usuarios_grupos.html'
    context_object_name = 'usuarios_grupos'             # permite cambiar de nombre al objetos listview que se llamara en la vista
    queryset=  User.objects.all().values('username',"groups__name", "perfil__puesto")           #  Permite realizar filtros a la consulta
    
    @method_decorator(login_required)             #Puede agrupar decoradores
    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('productos.view_productos'):
        #       messages.success(request,"ACCESO DENEGADO")
        #       return redirect('home')
        #print(Perfil.objects.select_related('user').query)
        #print(User.objects.prefetch_related('username').query)
        # print(Group.users.all())

        return super( ListadoUsuario_Grupo,self).dispatch(request, *args, **kwargs)
    


