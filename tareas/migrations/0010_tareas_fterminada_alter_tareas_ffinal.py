# Generated by Django 4.2 on 2023-06-07 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0009_rename_asignada_tareas_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tareas',
            name='Fterminada',
            field=models.DateTimeField(blank=True, help_text='fecha final', null=True),
        ),
        migrations.AlterField(
            model_name='tareas',
            name='Ffinal',
            field=models.DateField(help_text='fecha plazo'),
        ),
    ]