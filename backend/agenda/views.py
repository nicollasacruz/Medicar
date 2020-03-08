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
        field_name="especialidade_especialidade", 
        lookup_expr="icontains",
        queryset = Especialidade.objects.all())
    data_inicio = filters.DateFilter(field_name="dia", lookup_expr='dia__gte')
    data_final = filters.DateFilter(field_name="dia", lookup_expr='dia__lte')

    class Meta:
        model = Agenda
        fields = ['medico', 'especialidade', 'data_inicio', 'data_final']


class AgendaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = AgendaFilter
    ordering_fields = ('dia',)

    def list(self, request):
        queryset = Agenda.objects.all()
        serializer = AgendaSerializer(queryset, many=True)
        for obj in queryset:
            if obj.dia < datetime.date.today():
                Agenda.objects.get(id=obj.id).delete()
            return Response(serializer.data)
