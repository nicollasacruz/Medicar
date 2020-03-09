from django.contrib import admin
from agenda.models import Horario
from agenda.models import Agenda
from agenda.forms import AgendaAdminForm

# Register your models here.
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('horario',)


class AgendaAdmin(admin.ModelAdmin):
    form = AgendaAdminForm
    list_display = ['medico','dia', 'horarios']
    autocomplete_fields = ["medico"]


admin.site.register(Horario)
admin.site.register(Agenda, AgendaAdmin)
