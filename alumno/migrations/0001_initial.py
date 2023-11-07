# Generated by Django 4.2.6 on 2023-11-06 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('idalumno', models.AutoField(primary_key=True, serialize=False)),
                ('rut', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('carrera', models.CharField(max_length=60)),
                ('fechaDeNacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]