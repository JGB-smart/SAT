from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from tareas.models import  ArchivoTareas

from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DeleteView, View

# Create your views here.

class ListadoCalificacion(ListView):
    model = ArchivoTareas
    template_name = 'calificaciones_tarea.html'
    context_object_name = 'tareas'             # permite cambiar de nombre al objetos listview que se llamara en la vista
    queryset=  ArchivoTareas.objects.all()           #  Permite realizar filtros a la consulta
                                              # PROBAR:REMPLAZAR QUERYSET por su metodo de este modo:
                                                ## def get_queryset(self):
                                                ##  return self.model.objects.filter(fitrodecampo)   
                                                
    @method_decorator(login_required)             #Puede agrupar decoradores
    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('productos.view_productos'):
        #       messages.success(request,"ACCESO DENEGADO")
        #       return redirect('home')
        #print(Perfil.objects.select_related('user').query)
        #print(User.objects.prefetch_related('username').query)
        # print(Tareas.objects.all().values('categorias__categoria'))

        return super( ListadoCalificacion,self).dispatch(request, *args, **kwargs)