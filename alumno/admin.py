from django.contrib import admin
from alumno.forms import AlumnoForm
from alumno.models import Alumno, Inscripcion

class AlumnoAdminForm(AlumnoForm):
    class Meta(AlumnoForm.Meta):
        model = Alumno

class InscripcionInline(admin.TabularInline):
    model = Inscripcion
    extra = 1

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ['rut', 'nombre', 'apellido', 'carrera', 'fechaDeNacimiento', 'email', 'get_ramos_display']
    inlines = [InscripcionInline]
    list_filter = ['carrera', 'inscripcion__ramo__nombre']  
    def get_ramos_display(self, obj):
        return ', '.join([inscripcion.ramo.nombre for inscripcion in obj.inscripcion_set.all()])

    get_ramos_display.short_description = 'Ramos'

admin.site.register(Alumno, AlumnoAdmin)
