from django.contrib import admin
from formularioRamos.models import Ramos
from formularioRamos.forms import RamosForm

class RamosAdminForm(RamosForm):
    class Meta(RamosForm.Meta):
        model = Ramos

class RamosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'carrera', 'descripcion', 'creditos', 'horas', 'sala']
    form = RamosAdminForm

admin.site.register(Ramos, RamosAdmin)