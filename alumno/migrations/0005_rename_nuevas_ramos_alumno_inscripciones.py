# Generated by Django 4.2.6 on 2023-11-18 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno', '0004_remove_alumno_ramos_alumno_nuevas_ramos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='nuevas_ramos',
            new_name='inscripciones',
        ),
    ]
