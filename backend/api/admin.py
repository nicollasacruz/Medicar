from django.contrib import admin
from api.models import Especialidade
from api.models import Medico
from api.models import Agenda


class EspecialidadeAdmin(admin.ModelAdmin):
    fields = ['nome']


class MedicoAdmin(admin.ModelAdmin):
    fields = ['nome', 'crm', 'email', 'telefone', 'especialidade']


class AgendaAdmin(admin.ModelAdmin):
    fields = ['dia', 'medico', 'horarios']
    

admin.site.register(Especialidade)
admin.site.register(Medico)
admin.site.register(Agenda)





# Register your models here.
# class EspecialidadeForm(forms.ModelForm):
#     class Meta:
#         model = Especialidade
#         fields = ('__all__')


# class MedicoForm(forms.ModelForm):
#     class Meta:
#         model = Medico
#         fields = ('__all__')

# class AgendaForm(forms.ModelForm):
#     class Meta:
#         model = Agenda
#         fields = ('__all__')