# Generated by Django 4.1.2 on 2022-10-04 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='permisos',
            fields=[
                ('id_rol', models.IntegerField(max_length=30, primary_key=True, serialize=False)),
                ('nombre_permiso', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='personas',
            fields=[
                ('us_id', models.IntegerField(max_length=30, primary_key=True, serialize=False)),
                ('primer_nombre', models.CharField(max_length=32)),
                ('segundo_nombre', models.CharField(blank=True, max_length=32, null=True)),
                ('primer_apellido', models.CharField(max_length=32)),
                ('segundo_apellido', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.EmailField(max_length=32, unique=True)),
                ('nro_telefono', models.CharField(max_length=32, unique=True)),
                ('psw', models.CharField(max_length=128)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='roles',
            fields=[
                ('id_rol', models.IntegerField(max_length=30, primary_key=True, serialize=False)),
                ('nombre_rol', models.CharField(max_length=32, unique=True)),
                ('personas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='inventario.personas')),
            ],
        ),
        migrations.CreateModel(
            name='roles_permisos',
            fields=[
                ('id_roles_permisos', models.IntegerField(max_length=30, primary_key=True, serialize=False)),
                ('permisos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roles_permisos', to='inventario.permisos')),
                ('roles', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roles_permisos', to='inventario.roles')),
            ],
        ),
        migrations.CreateModel(
            name='activo',
            fields=[
                ('id_activo', models.IntegerField(max_length=30, primary_key=True, serialize=False)),
                ('nombre_activo', models.CharField(max_length=32, unique=True)),
                ('cantidad', models.IntegerField(max_length=30)),
                ('precio', models.CharField(max_length=32, unique=True)),
                ('roles', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='activo', to='inventario.roles')),
            ],
        ),
    ]
