from django.contrib import admin
from .models import Comentarios

# Register your models here.

@admin.register(Comentarios)
class OilPriceHistoryAdmin(admin.ModelAdmin):
    model = Comentarios
    list_display = ['tarea','comentario','user','fecha']