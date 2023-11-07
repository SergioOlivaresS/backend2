from django.contrib import admin
from alumno.forms import AlumnoForm
from alumno.models import Alumno
from django import forms

class AlumnoAdminForm(AlumnoForm):
    class Meta(AlumnoForm.Meta):
        model = Alumno

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'carrera', 'fechaDeNacimiento', 'email']
    form = AlumnoAdminForm  # Establece el formulario personalizado

admin.site.register(Alumno, AlumnoAdmin)
