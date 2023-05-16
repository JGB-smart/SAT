from django.db import models

class Categorias(models.Model):
    
    categoria = models.CharField(max_length=150,verbose_name='categoria')

    def __str__(self):
        return "categoria:" + self.categoria

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['-id']  
