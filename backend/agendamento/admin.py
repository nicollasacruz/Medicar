from django.contrib import admin
from agendamento.models import Especialidade
from agendamento.models import Medico
from agendamento.models import Agenda
from agendamento.forms import AgendaAdminForm


class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ['nome']
    fields = ['nome']


class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'email', 'telefone', 'especialidade')
    list_filter = ['especialidade']
    search_fields = ['nome']


class AgendaAdmin(admin.ModelAdmin):
    form = AgendaAdminForm
    list_display = ('medico', 'dia')
    autocomplete_fields = ["medico"]


admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidade, EspecialidadeAdmin)
admin.site.register(Agenda, AgendaAdmin)
