from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DeleteView, View
from django.contrib import messages

from .forms import TareasForm
from .forms import TareasForm2

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
    autorizacion = 0

    def get(self,request):
        # form = TareasForm()

        rol = request.user.groups.all().values('name')
        verifica = Autorizacion(rol)

        
        
        if verifica == 1:
            form = TareasForm()
            return render(request,self.template_name,{"form":form})
        if verifica == 2:
            form = TareasForm()
            return render(request,self.template_name,{"form":form})    
        if verifica == 3:
            form = TareasForm2()
            return render(request,self.template_name,{"form":form})
        
        

    def post(self,request):
        
        rol = request.user.groups.all().values('name')
        verifica = Autorizacion(rol) 
        
        if verifica == 1:
            form = TareasForm(request.POST)

            
            if form.is_valid():
                # form.save()
                
                post = form.save(commit = False)
                post.CreadaPor_id = request.user.id
                
                if post.porcentaje > 100 :
                    post.porcentaje = 100
                else:
                    post.porcentaje = 0

                post.save()

                #  Logica para guardar un Form.form
                # if form.is_valid():
                #     campo = form.cleaned_data['nombredelcampo']
                #     Tabla.objects.create(campo =  campo )

                messages.success(request,"Tarea Creada")
                return redirect('lista_tareas')
            else:
            
                # for msg in form.error_messages:
                #     messages.error(request, form.error_messages[msg])

                return render(request,self.template_name,{"form":form})
        
        if verifica == 2:
            form = TareasForm(request.POST)

            
            if form.is_valid():
                # form.save()
                
                post = form.save(commit = False)
                post.CreadaPor_id = request.user.id
                
                if post.porcentaje > 100 :
                    post.porcentaje = 100
                else:
                    post.porcentaje = 0

                post.save()

                #  Logica para guardar un Form.form
                # if form.is_valid():
                #     campo = form.cleaned_data['nombredelcampo']
                #     Tabla.objects.create(campo =  campo )

                messages.success(request,"Tarea Creada")
                return redirect('lista_tareas')
            else:
            
                # for msg in form.error_messages:
                #     messages.error(request, form.error_messages[msg])

                return render(request,self.template_name,{"form":form})
                   
        if verifica == 3:
            form = TareasForm2(request.POST)

            
            if form.is_valid():
                # form.save()
                
                post = form.save(commit = False)
                post.CreadaPor_id = request.user.id
                post.user_id = request.user.id
                if post.porcentaje > 100 :
                    post.porcentaje = 100
                else:
                    post.porcentaje = 0

                post.save()

                #  Logica para guardar un Form.form
                # if form.is_valid():
                #     campo = form.cleaned_data['nombredelcampo']
                #     Tabla.objects.create(campo =  campo )

                messages.success(request,"Tarea Creada")
                return redirect('lista_tareas')
            else:
            
                # for msg in form.error_messages:
                #     messages.error(request, form.error_messages[msg])

                return render(request,self.template_name,{"form":form})
            
              
        
        
        # form = TareasForm(request.POST)

        
        # if form.is_valid():
        #     # form.save()
            
        #     post = form.save(commit = False)
        #     post.CreadaPor_id = request.user.id
            
        #     if post.porcentaje > 100 :
        #         post.porcentaje = 100
        #     else:
        #         post.porcentaje = 0

        #     post.save()

        #     #  Logica para guardar un Form.form
        #     # if form.is_valid():
        #     #     campo = form.cleaned_data['nombredelcampo']
        #     #     Tabla.objects.create(campo =  campo )

        #     messages.success(request,"Tarea Creada")
        #     return redirect('lista_tareas')
        # else:
        
        #     # for msg in form.error_messages:
        #     #     messages.error(request, form.error_messages[msg])
            
        #     return render(request,self.template_name,{"form":form})
    



def Autorizacion(rol):                                     # Método que verifica el rol del usuario


        Directores = ['Directores']
        Gerentes = ['Gerentes']
        Trabajadores = ['Trabajadores']
        
        for grupo in rol:
            if grupo['name'] in Directores:

                return 1
            if grupo['name'] in Gerentes:

                return 2  
            if grupo['name'] in Trabajadores:

                return 3
