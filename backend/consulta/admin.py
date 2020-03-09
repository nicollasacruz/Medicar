from django.contrib import admin
from consulta.models import Consulta

# Register your models here.
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['dia','horario', 'especialidade', 'medico', 'data_agendamento']
    autocomplete_fields = ['medico', 'especialidade']    

admin.site.register(Consulta, ConsultaAdmin)

