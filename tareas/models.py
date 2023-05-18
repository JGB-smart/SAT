from django.db import models
from categorias.models import Categorias
from django.contrib.auth.models import User

class Status(models.Model):
    status = models.CharField(max_length=150,verbose_name='status')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'
        ordering = ['-id']  

class Prioridad(models.Model):
    prioridad = models.CharField(max_length=150,verbose_name='prioridad')

    def __str__(self):
        return self.prioridad

    class Meta:
        verbose_name = 'Prioridad'
        verbose_name_plural = 'Prioridades'
        ordering = ['-id']  

class Tareas(models.Model):

    tarea =  models.CharField(max_length=150,verbose_name='tarea')
    descripcion =  models.CharField(max_length=200,verbose_name='descripcion')
    status = models.ForeignKey(Status, on_delete=models.CASCADE,related_name='status_tarea')
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE,related_name='prioridad_tarea')
    categoria = models.ForeignKey(Categorias,on_delete=models.CASCADE, related_name='categorias_tarea')
    porcentaje = models.IntegerField(default=0)
    CreadaPor = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'creador_tarea')
    asignada = models.ForeignKey(User,on_delete=models.CASCADE,related_name = 'asignaciones')
    Fcreacion = models.DateTimeField(auto_now_add=True)
    Ffinal = models.DateField()

    def __str__(self):
        return self.tarea

    class Meta:
        verbose_name = 'Tarea'
        verbose_name_plural = 'Tareas'
        ordering = ['-id']  



