# Generated by Django 4.2 on 2023-06-19 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0013_rename_calificaon_archivotareas_calificacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tareas',
            name='Fcreacion',
            field=models.DateField(auto_now_add=True),
        ),
    ]
