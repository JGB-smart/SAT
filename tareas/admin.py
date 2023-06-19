from django.contrib import admin
from .models import Status
from .models import Prioridad
from .models import Tareas, ArchivoTareas

# Register your models here.
admin.site.register(Status)
admin.site.register(Prioridad)
# admin.site.register(Tareas)

@admin.register(Tareas)
class TareasAdmin(admin.ModelAdmin):
    model = Tareas
    list_display = ['tarea','Ffinal','status','prioridad','categoria']



@admin.register(ArchivoTareas)
class ArchivoTareasAdmin(admin.ModelAdmin):
    model = Tareas
    list_display = ['tarea','Ffinal','status','prioridad','categoria']