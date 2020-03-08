from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from agenda.models import Agenda
from medico.models import Medico
from especialidade.models import Especialidade
from agenda.serializers import AgendaSerializer


class AgendaFilter(filters.FilterSet):
    medico = filters.ModelMultipleChoiceFilter(
        queryset=Medico.objects.all())
    especialidade = filters.ModelMultipleChoiceFilter(
        queryset = Especialidade.objects.all())

    class Meta:
        model = Agenda
        fields = ['medico', 'especialidade']



class AgendaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AgendaFilter

