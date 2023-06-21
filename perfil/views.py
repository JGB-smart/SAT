from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from tareas.views import Autorizacion

from django.contrib.auth.models import User
from perfil.models import Perfil
from tareas.models import ArchivoTareas
from tareas.models import Tareas
from django.db.models import Sum



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
