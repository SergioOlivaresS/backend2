from django.contrib import admin
from formularioRamos.models import Ramos
from formularioRamos.forms import RamosForm

class RamosAdminForm(RamosForm):
    class Meta(RamosForm.Meta):
        model = Ramos

class RamosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'carrera', 'descripcion', 'creditos', 'horas', 'sala', 'profesor_display']
    form = RamosAdminForm

    def profesor_display(self, obj):
        return str(obj.profesor)
    profesor_display.short_description = 'Profesor'

admin.site.register(Ramos, RamosAdmin)