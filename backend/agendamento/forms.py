from django import forms
from agendamento.models import Agenda
from datetime import datetime
from django.contrib import messages

class AgendaAdminForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'
    
    def clean(self):
        cleaned_data = self.cleaned_data
        # if str(cleaned_data.dia) 
        # print(cleaned_data)
        # department = cleaned_data.get('department')
        # isDepartmentSuggested = cleaned_data.get('isDepartmentSuggested')
        # if department == None and not isDepartmentSuggested:
        #     raise forms.ValidationError(u"You haven't set a valid department. Do you want to continue?")
        return cleaned_data

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     department = cleaned_data.get('department')
    #     isDepartmentSuggested = cleaned_data.get('isDepartmentSuggested')
    #     if department == None and not isDepartmentSuggested:
    #         raise forms.ValidationError(u"You haven't set a valid department. Do you want to continue?")
    #     return cleaned_data