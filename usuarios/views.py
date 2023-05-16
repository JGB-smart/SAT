from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DeleteView, View
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from .forms import RegistrationGroupForm

from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from perfil.models import Perfil


# @method_decorator(login_required, name="dispatch") PROBAR: Manera de colocar un decorator en una clase
class ListadoUsuarios(ListView):
    model = User
    template_name = 'lista_usuarios.html'
    context_object_name = 'usuarios'             # permite cambiar de nombre al objetos listview que se llamara en la vista
    queryset=  User.objects.all()           #  Permite realizar filtros a la consulta
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
    

class AgregarUsuario(View):
    
    template_name = 'agg_usuarios.html'
    # Model = User
    

    def get(self,request):
        form = RegistrationForm()
        form2 = RegistrationGroupForm()
        
        return render(request,self.template_name,{"form":form, "form2":form2})
    

    def post(self,request):
        form = RegistrationForm(request.POST)
        form2 = RegistrationGroupForm()
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(id= request.POST['grupo'])
            user.groups.add(group)
            messages.success(request,"Usuario registrado")
            return redirect('lista_usuarios')
        else:
        
            # for msg in form.error_messages:
            #     messages.error(request, form.error_messages[msg])
            
            return render(request,self.template_name,{"form":form, "form2":form2})
    

class EditarUsuario(UpdateView):
    model = User
    form_class = RegistrationForm
    template_name = 'agg_usuarios.html'
    success_url= reverse_lazy('lista_usuarios')
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # if not request.user.has_perm('productos.change_productos'):
        #       messages.success(request,"ACCESO DENEGADO")
        #       return redirect('productos')
        return super(EditarUsuario,self).dispatch(request, *args, **kwargs)



def EliminarUsuario(request, pk):
    user = get_object_or_404(User, id = pk)
    user.delete()
    messages.success(request,"Usuario eliminado")
    return redirect('lista_usuarios')