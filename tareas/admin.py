from django.contrib import admin
from .models import Status
from .models import Prioridad
from .models import Tareas

# Register your models here.
admin.site.register(Status)
admin.site.register(Prioridad)
admin.site.register(Tareas)