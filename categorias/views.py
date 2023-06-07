from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DeleteView, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from categorias.models import Categorias

from .forms import CategoriasForm







class ListadoCategorias(ListView):
    model = Categorias
    template_name = 'lista_categorias.html'
    context_object_name = 'categorias'             # permite cambiar de nombre al objetos listview que se llamara en la vista
    queryset=  Categorias.objects.all()           #  Permite realizar filtros a la consulta
                                              # PROBAR:REMPLAZAR QUERYSET por su metodo de este modo:
                                                ## def get_queryset(self):
                                                ##  return self.model.objects.filter(fitrodecampo)   
                                                
    @method_decorator(login_required)             #Puede agrupar decoradores
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('categorias.view_categorias'):
              messages.success(request,"ACCESO DENEGADO")
              return redirect('lista_tareas')
        #print(Perfil.objects.select_related('user').query)
        #print(User.objects.prefetch_related('username').query)
        # print(Group.users.all())

        return super( ListadoCategorias,self).dispatch(request, *args, **kwargs)
    

class AgregarCategoria(View):
    
    template_name = 'agg_categorias.html'
    # Model = User
    

    def get(self,request):
        form = CategoriasForm()
        
        return render(request,self.template_name,{"form":form})
    

    def post(self,request):
        form = CategoriasForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,"Categoría agregada")
            return redirect('lista_categorias')
        else:        
            #  for msg in form.error_messages:
            #     messages.error(request, form.error_messages[msg])
            return render(request,self.template_name,{"form":form,})

    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('categorias.add_categorias'):
              messages.success(request,"ACCESO DENEGADO")
              return redirect('lista_tareas')

        return super( AgregarCategoria,self).dispatch(request, *args, **kwargs)    



@login_required
def EliminarCategoria(request, pk):

    
    if not request.user.has_perm('categorias.delete_categorias'):
              messages.success(request,"ACCESO DENEGADO")
              return redirect('lista_tareas')
    else:
        categoria = get_object_or_404(Categorias, id = pk)
        categoria.delete()
        messages.success(request,"Categoría eliminada")
        return redirect('lista_categorias')





class EditarCategoria(UpdateView):
    model = Categorias
    form_class =  CategoriasForm
    template_name = 'agg_categorias.html'
    success_url= reverse_lazy('lista_categorias')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('categorias.change_categorias'):
              messages.success(request,"ACCESO DENEGADO")
              return redirect('lista_tareas')
        return super(EditarCategoria,self).dispatch(request, *args, **kwargs)