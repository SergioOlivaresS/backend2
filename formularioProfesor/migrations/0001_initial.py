# Generated by Django 4.2.7 on 2023-11-14 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RUT', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('Telefono', models.IntegerField()),
                ('Area', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'profesores',
            },
        ),
    ]