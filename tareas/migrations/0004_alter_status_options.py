# Generated by Django 4.2 on 2023-05-17 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tareas', '0003_alter_tareas_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['-id'], 'verbose_name': 'Status', 'verbose_name_plural': 'Status'},
        ),
    ]