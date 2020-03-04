from django.contrib import admin
# from .models import Especialidade
from .models import Medico
from .models import Agenda
from .models import Horario
from .forms import AgendaAdminForm


class HorarioAdmin(admin.ModelAdmin):
    list_display = ('horario',)


# class EspecialidadeAdmin(admin.ModelAdmin):
#     list_display = ('nome',)
#     search_fields = ['nome']
#     fields = ['nome']


class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'email', 'telefone', 'especialidade')
    list_filter = ['especialidade']
    search_fields = ['nome']


class AgendaAdmin(admin.ModelAdmin):
    form = AgendaAdminForm
    list_display = ('medico', 'dia', 'get_horarios')
    autocomplete_fields = ["medico"]


admin.site.register(Medico, MedicoAdmin)
# admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Horario)
