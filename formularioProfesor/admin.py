from django.contrib import admin
from formularioProfesor.models import Profesor
from formularioProfesor.forms import ProfesorForm

class ProfesorAdminForm(ProfesorForm):
    class Meta(ProfesorForm.Meta):
        model = Profesor

class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['RUT', 'nombre', 'apellido', 'Telefono', 'Area', 'Email']
    form = ProfesorAdminForm

admin.site.register(Profesor, ProfesorAdmin)