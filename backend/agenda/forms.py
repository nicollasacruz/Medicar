from django import forms
from agenda.models import Agenda
from agenda.models import Horario
import datetime


class AgendaAdminForm(forms.ModelForm):
    horario = forms.ModelMultipleChoiceField(queryset=Horario.objects.all(), required=False)

    class Meta:
        model = Agenda
        fields = '__all__'

    def clean_dia(self):
        dia = self.cleaned_data['dia']
        if dia < datetime.date.today():
            raise forms.ValidationError("O dia da agenda não pode ser um data passada")
        return dia
    