from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='perfil')
    image = models.ImageField(default='users/image_user.png', upload_to='users/')
    telf = models.BigIntegerField(null= True, blank=True)
    puesto = models.CharField(max_length=50, null= True, blank=True)

    def __str__(self):
        return "user: " + str(self.user)

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()

post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)