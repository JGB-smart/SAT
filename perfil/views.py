from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from tareas.views import Autorizacion
from django.contrib import messages

from django.contrib.auth.models import User
from perfil.models import Perfil
from tareas.models import ArchivoTareas
from tareas.models import Tareas
from django.db.models import Sum


from perfil.forms import EditUserForm,EditPerfilForm



@login_required
def Perfil_Usuario(request,pk):

    if request.method == 'GET':

        usuario = get_object_or_404(User,id=pk)      # Obtención del usuario
        
        rol = usuario.groups.all().values('name') # Obtención del rol del usuario
        grups = Autorizacion(rol)

        if grups == 1:
            grupo = 'Director'
        elif grups == 2:
            grupo = 'Gerente'
        elif grups == 3:
            grupo = 'Trabajador'
        else:
            grupo = 'Desconocido'        
        
        # Obtención del puntaje del usuario
        puntaje = ArchivoTareas.objects.all().filter(user_id = pk).aggregate(Sum('calificacion'))  

        if puntaje.get('calificacion__sum'):
            puntos = puntaje.get('calificacion__sum')
        else:
            puntos = 0
                 
        
        tareas_activas = Tareas.objects.all().filter(user_id = pk).count()
        tareas_archivadas = ArchivoTareas.objects.all().filter(user_id = pk).count()
        
        data = {
            'usuario': usuario,
            'grupo' : grupo,
            'puntaje' : puntos,
            'tareas_activas': tareas_activas,
            'tareas_archivadas': tareas_archivadas
        }


        return render(request,'perfil.html',data)

def Editar_Usuario(request, pk):

    usuario = get_object_or_404(User,id = pk)
    perfil = get_object_or_404(Perfil,id = pk)


    data = {
        'form1': EditUserForm(instance = usuario),
        'form2': EditPerfilForm(instance = perfil),
        'usuario': usuario,

    }


    if request.method == 'GET':


        return render(request,'editar_perfil.html',data)
    
    elif request.method == 'POST':

        form1 = EditUserForm(data = request.POST, instance=usuario,files = request.FILES)
        form2 = EditPerfilForm(data = request.POST, instance=perfil,files = request.FILES)

        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()

            
            messages.success(request,"Usuario Editado")
            return redirect('perfil',usuario.id)
        else:
            messages.error(request,"Ha Ocurrido un error!")
            return render(request,'editar_perfil.html',data)


    