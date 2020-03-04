from django import forms
from agenda.models import Agenda
import datetime


class AgendaAdminForm(forms.ModelForm):

    class Meta:
        model = Agenda
        fields = '__all__'

    def clean_dia(self):
        dia = self.cleaned_data['dia']
        if dia < datetime.date.today():
            raise forms.ValidationError("O dia da agenda não pode ser um data passada")
        return dia
    