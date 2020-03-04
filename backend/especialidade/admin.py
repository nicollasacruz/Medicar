from django.contrib import admin
from especialidade.models import Especialidade

# Register your models here.
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ['nome']
    fields = ['nome']

admin.site.register(Especialidade, EspecialidadeAdmin)
