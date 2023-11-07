from django.contrib import admin
from alumno.models import Alumno


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'carrera', 'fechaDeNacimiento', 'email']

admin.site.register(Alumno)
