# Generated by Django 4.0.1 on 2022-11-10 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0007_alter_maquinaria_material_estructura'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='maquinaria',
            new_name='maquinariac',
        ),
        migrations.RenameField(
            model_name='herramientas',
            old_name='activo',
            new_name='activoh',
        ),
        migrations.RenameField(
            model_name='maquinaria',
            old_name='activo',
            new_name='activom',
        ),
    ]
