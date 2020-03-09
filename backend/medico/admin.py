from django.contrib import admin
from medico.models import Medico

# Register your models here.
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'crm', 'email', 'telefone', 'especialidade')
    list_filter = ['especialidade']
    search_fields = ['nome']


admin.site.register(Medico, MedicoAdmin)
