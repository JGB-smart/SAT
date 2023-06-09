# Generated by Django 4.2 on 2023-05-17 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prioridad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prioridad', models.CharField(max_length=150, verbose_name='prioridad')),
            ],
            options={
                'verbose_name': 'Prioridad',
                'verbose_name_plural': 'Prioridades',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='T_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=150, verbose_name='status')),
            ],
            options={
                'verbose_name': 'T_Status',
                'verbose_name_plural': 'T_Status',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarea', models.CharField(max_length=150, verbose_name='tarea')),
                ('descripcion', models.CharField(max_length=200, verbose_name='descripcion')),
                ('porcentaje', models.IntegerField()),
                ('CreadaPor', models.CharField(max_length=150, verbose_name='tarea')),
                ('Fcreacion', models.DateTimeField(auto_now_add=True)),
                ('Ffinal', models.DateTimeField()),
                ('Asignada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaciones', to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categorias_tarea', to='categorias.categorias')),
                ('prioridad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prioridad_tarea', to='tareas.prioridad')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_tarea', to='tareas.t_status')),
            ],
        ),
    ]
