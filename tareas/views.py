# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from datetime import datetime

from tareas.models import Tareas,Status,Prioridad, ArchivoTareas
from categorias.models import Categorias
from django.contrib.auth.models import User

from django.views.generic import TemplateView,ListView, CreateView, UpdateView, DeleteView, View

from tareas.forms import TareasForm
from tareas.forms import TareasForm2


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


class ListadoArchivoTareas(ListView):
    '''
    List Vire que devuelve la lista de las tareas archivadas en la tabla de archivo muerto
    '''
    model = ArchivoTareas
    template_name = 'lista_archivo.html'
    context_object_name = 'archivo'   
    queryset=  ArchivoTareas.objects.all() 
                                                
    @method_decorator(login_required)         
    def dispatch(self, request, *args, **kwargs):
        return super( ListadoArchivoTareas,self).dispatch(request, *args, **kwargs)



class CrearTarea(View):
    
    template_name = 'agg_tarea.html'
    Model = Tareas
    autorizacion = 0

    def get(self,request):
        # form = TareasForm()

        rol = request.user.groups.all().values('name')
        verifica = Autorizacion(rol)

        
        print(verifica)
        if verifica == 1:
            form = TareasForm()
            return render(request,self.template_name,{"form":form})
        if verifica == 2:
            form = TareasForm()
            return render(request,self.template_name,{"form":form})    
        if verifica == 3:
            form = TareasForm2()
            return render(request,self.template_name,{"form":form})
        else:
            return redirect('lista_tareas')
        
        

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
                
                
                # if not post.status_id:                            # Creacion del status inicial por default
                    
                #     post.status_id = 1                           


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

                if not post.status_id:                            # Creacion del status inicial por default
                    
                    post.status_id = 1                           


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

                if not post.status_id:                            # Creacion del status inicial por default
                    
                    post.status_id = 1                           


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
        else:
            return redirect('lista_tareas')    
              
        
        
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
    



def EliminarTarea(request, pk):
    tarea = get_object_or_404(Tareas, id = pk)
    rol = request.user.groups.all().values('name')
    verifica = Autorizacion(rol)
    verifica_tarea = Tarea_Autorizacion(pk)
    

    if verifica == 1:
        tarea.delete()
        messages.success(request,"Tarea eliminada")
        return redirect('lista_tareas')
    if verifica == 2: 
        if verifica_tarea == 1:
            messages.error(request,"No esta Autorizado para realizar esta acción!") 
            return redirect('lista_tareas')
        if verifica_tarea == 2 and tarea.CreadaPor == request.user:    
            messages.success(request,"Tarea eliminada")
            return redirect('lista_tareas')
        elif verifica_tarea == 3:
            tarea.delete()
            messages.success(request,"Tarea eliminada")
            return redirect('lista_tareas')
        else:
            messages.error(request,"No esta Autorizado para realizar esta acción!")    
            return redirect('lista_tareas')
    else:
        messages.error(request,"No esta Autorizado para realizar esta acción!")
        return redirect('lista_tareas')


@login_required
def EditarTarea(request, pk):
    
    tarea = get_object_or_404(Tareas,id = pk)                                       # obtencion del objeto
    
    rol = request.user.groups.all().values('name')                                  #3 Verificaion del Rol
    verifica = Autorizacion(rol)
    verifica_tarea = Tarea_Autorizacion(pk)

    if verifica == 1 or verifica == 2 or tarea.user == request.user:                   # Verificaion del rol o del usuario asignado
        
        if verifica == 1 or verifica == 2:                                             # Condicional que control el form que pinta el get
            data = {
                    'form': TareasForm(instance=tarea)
                }
        else:
            data = {
                    'form': TareasForm2(instance=tarea)
                } 


        if verifica == 2 and verifica_tarea == 1:                                    ## Condicional que controla el acceso de gerente a tareas hechas por un director
            if not tarea.user == request.user:
                messages.error(request,"No esta Autorizado para realizar esta acción!")    
                return redirect('lista_tareas')

        if request.method == 'GET':
            

            return render(request,'editar_tarea.html',data)
        
        elif request.method == 'POST':
            if verifica == 1:
                form = TareasForm(data = request.POST, instance=tarea,files=request.FILES)
            elif verifica == 2:                                              # Condicional que controla el form que guarda el post
                tarea_status = get_object_or_404(Status,id = request.POST['status'])
                asignado = get_object_or_404(User,id = request.POST['user'])
                if(tarea.user == request.user and (tarea_status.status == 'Revisión' or tarea_status.status == 'Finalizada' or tarea_status.status == 'Re_abierta')):
                    messages.error(request,"Su nivel de usuario no se puede autoevaluar")    
                    return redirect('lista_tareas')
                elif verifica_tarea == 1 and tarea.user == request.user:
                    if not asignado == request.user:
                        messages.error(request,"No tiene permiso para reasignar esta tarea")    
                        return redirect('lista_tareas')
                    else:
                        form = TareasForm(data = request.POST, instance=tarea,files=request.FILES)
                # elif verifica_tarea == 1 and tarea.user == request.user:
                #     if request.POST['user'] == request.user.id:
                #         messages.error(request,"No tiene permisos para reasignar esta tarea")    
                #         return redirect('lista_tareas')  
                else:
                    form = TareasForm(data = request.POST, instance=tarea,files=request.FILES)
                    # print(request.POST['user'])
            else:
                form = TareasForm2(data = request.POST, instance=tarea,files=request.FILES)
            
            if form.is_valid():
                form.save()
                messages.success(request,"Tarea Editada")

                tarea_status = get_object_or_404(Status,id = request.POST['status'])

                if(tarea_status.status != 'Finalizada'):
                    return redirect('lista_tareas')
                else:

                    # Respaldar los valores al hitórico
                    At = ArchivoTareas(
                        tarea = tarea.tarea,
                        descripcion = tarea.descripcion,
                        status = tarea.status,
                        prioridad = tarea.prioridad,
                        categoria = tarea.categoria,
                        porcentaje = tarea.porcentaje,
                        CreadaPor = tarea.CreadaPor,
                        user = tarea.user,
                        Fcreacion = tarea.Fcreacion,
                        Ffinal = tarea.Ffinal,
                        Fterminada = datetime.now()
                        )

                    At.save()

                    # Borrar la tarea de la tabla principal
                    delete_tarea = Tareas.objects.get(pk=tarea.pk)
                    delete_tarea.delete()

                    # Retornar la lista de nuevo
                    tareas=  Tareas.objects.all() 
                    return render(request,'lista_tareas.html',{
                        'tareas':tareas,
                        'messages':False,
                        'archived':At.pk})

            else:
                messages.error(request,"Ha Ocurrido un error!")
                data['form'] = form
                return render(request,'editar_tarea.html',data)
    else:
        messages.error(request,"No esta Autorizado para realizar esta acción!")
        return redirect('lista_tareas')    
   



        # if verifica == 1:                                                               # Condicionales de Segundo Control de acceso que comprueba quien tiene acesso a la tarea 
        #     if request.method == 'GET':                   
        #         return render(request,'editar_tarea.html',data)       
        
        # if verifica == 2:
     
     
        #     if verifica_tarea == 2 and tarea.CreadaPor == request.user:                # Caso de creación propia del gerente
        #         if request.method == 'GET':                   
        #             return render(request,'editar_tarea.html',data)
        #     if tarea.user == request.user:                                             # Caso de asignacion al gerente
        #         if request.method == 'GET':                   
        #             return render(request,'editar_tarea.html',data)
                    
     
        #     if verifica_tarea == 1:
        #         messages.error(request,"No esta Autorizado para realizar esta acción!")    
        #         return redirect('lista_tareas')        
            
            
        #     if verifica_tarea == 3:
        #         if request.method == 'GET':                   
        #             return render(request,'editar_tarea.html',data)
        #     else:
        #         messages.error(request,"No esta Autorizado para realizar esta acción!")    
        #         return redirect('lista_tareas')

        # if verifica == 3:
        #     if request.method == 'GET':                   
        #         return render(request,'editar_tarea.html',data)





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






def Tarea_Autorizacion(pk):                                 # Metodo que verifica bajo que rol esta hecha una tarea

    tarea = Tareas.objects.filter(id = pk).values('tarea','CreadaPor__username','CreadaPor__groups__name')

    grupo = tarea[0]['CreadaPor__groups__name']


    if grupo == 'Directores':
        return 1
    if grupo == 'Gerentes':
        return 2
    if grupo == 'Trabajadores':
        return 3



    
    
    
    # Directores = ['Directores']
    # Gerentes = ['Gerentes']
    # Trabajadores = ['Trabajadores']
        
    # for grupo in tarea[0]['CreadaPor__groups__name']:
    #     if grupo['name'] in Directores:

    #          return 1
    #     if grupo['name'] in Gerentes:

    #         return 2  
    #     if grupo['name'] in Trabajadores:

    #         return 3
    

class CalificarTarea(View):
    '''
    Vista para calificación de las tareas después de fimalizarlas (archivarlas)
    '''
    def post(self,request):
        tarea =  ArchivoTareas.objects.get(pk=request.POST['task']) 
        tarea.calificacion = request.POST['rating']
        tarea.save()

        return redirect('lista_tareas')
