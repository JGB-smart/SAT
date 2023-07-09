from django.db import models
from django.contrib.auth.models import User
from tareas.models import Tareas

class Comentarios(models.Model):
    comentario = models.CharField(max_length=300,verbose_name='comentario')
    tarea = models.ForeignKey(Tareas,on_delete = models.CASCADE,related_name='comentario_tarea')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'redactor')
    fecha = models.DateField(auto_now_add=True)

    

    class Meta:
        verbose_name = 'Comentarios'
        verbose_name_plural = 'Comentarios'
        ordering = ['id']  

