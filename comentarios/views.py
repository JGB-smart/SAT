from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DeleteView, View

from tareas.models import Tareas
from comentarios.models import Comentarios

from comentarios.forms import ComentariosForm

# Create your views here.


class ListadoTareas(ListView):
    model = Tareas
    template_name = 'comentario_tarea.html'
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





def comentarios(request, pk):

    if request.method == 'GET':

        comentarios = Comentarios.objects.filter(tarea_id = pk)
        tarea = get_object_or_404(Tareas,id = pk)

        titulo = tarea.tarea 
        categoria = tarea.categoria
        # comentarios = Comentarios.objects.all()

        data = {
            'comentarios': comentarios,
            'titulo': titulo,
            'categoria' : categoria,
            'form' : ComentariosForm()
        }

        return render(request,'lista_comentarios.html',data)
    
    elif request.method == 'POST':
        
        form = ComentariosForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.tarea_id = pk
            post.user_id = request.user.id
            post.save()
            return redirect('tarea_comentario')
        else:
            return render(request,'lista_comentarios.html')






# class Comentarios(View):
#     template_name = 'lista_comentarios.html'

#     def get(selft,request):

#         comentarios = Comentarios.objects.filter()

#         data = {
#             'comentarios': comentarios
#         }

#         return render(request, selft.template_name,data)