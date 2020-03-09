from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from consulta.models import Consulta
from medico.models import Medico
from especialidade.models import Especialidade
from consulta.serializers import ConsultaSerializer

class ConsultaFilter(filters.FilterSet):
    medico = filters.ModelMultipleChoiceFilter(
        queryset=Medico.objects.all())
    especialidade = filters.ModelMultipleChoiceFilter(
        queryset = Especialidade.objects.all())
    data_inicio = filters.DateFilter(field_name="dia", lookup_expr='dia__gte')
    data_final = filters.DateFilter(field_name="dia", lookup_expr='dia__lte')

    class Meta:
        model = Consulta
        fields = ['medico', 'especialidade', 'data_inicio', 'data_final']


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = ConsultaFilter
    ordering_fields = ('data_agendamento',)
