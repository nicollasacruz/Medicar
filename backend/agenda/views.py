from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from agenda.models import Agenda
from medico.models import Medico
from especialidade.models import Especialidade
from agenda.serializers import AgendaSerializer
import datetime


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
    ordering_fields = ('dia',)

    # def get(self, request, format=None):
    #     """
    #     Retorna todas as agendas.
    #     """
    #     agendas = [agenda.dia for agenda in Agenda.objects.all()]
    #     for agenda in agendas:

    #     print(agendas)
    #     return Response(agendas)

    def list(self, request):
        queryset = Agenda.objects.all()
        serializer = AgendaSerializer(queryset, many=True)
        for obj in queryset:
            if obj.dia < datetime.date.today():
                Agenda.objects.get(id=obj.id).delete()
            return Response(serializer.data)
