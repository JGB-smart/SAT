from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DeleteView, View
from django.contrib import messages

from .forms import TareasForm

from tareas.models import Tareas,Status,Prioridad
from categorias.models import Categorias
from django.contrib.auth.models import User

# Create your views here.


class ListadoTareas(ListView):
    model = Tareas
    template_name = 'lista_tareas.html'
    context_object_name = 'tareas'             # permite cambiar de nombre al objetos listview que se llamara en la vista
    queryset=  Tareas.objects.all()           #  Permite realizar filtros a la consulta
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

        return super( ListadoTareas,self).dispatch(request, *args, **kwargs)











class CrearTarea(View):
    
    template_name = 'agg_tarea.html'
    Model = Tareas
    

    def get(self,request):
        form = TareasForm()


        return render(request,self.template_name,{"form":form})
    

    def post(self,request):
        form = TareasForm(request.POST)

        if form.is_valid():
            # form.save()
            
            post = form.save(commit = False)
            post.CreadaPor_id = request.user.id
            post.save()

            # form.CreadaPor_id= request.user.id
            # form.save()
            messages.success(request,"Tarea Creada")
            return redirect('lista_tareas')
        else:
        
            # for msg in form.error_messages:
            #     messages.error(request, form.error_messages[msg])
            
            return render(request,self.template_name,{"form":form})