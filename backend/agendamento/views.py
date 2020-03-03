from django.shortcuts import render
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from agendamento.models import Especialidade
from agendamento.models import Medico
from agendamento.models import Agenda
from agendamento.serializers import EspecialidadeSerializer
from agendamento.serializers import MedicoSerializer
from agendamento.serializers import AgendaSerializer


class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    search_fields = ('nome',)

    def list(self, request):
        queryset = Especialidade.objects.all()
        serializer = EspecialidadeSerializer(queryset, many=True)
        return super(EspecialidadeViewSet, self).list(request,)


class MedicoViewSet(viewsets.ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    search_fields = ('nome',)

    def list(self, request):
        queryset = Medico.objects.all()
        serializer = MedicoSerializer(queryset, many=True)
        return super(MedicoViewSet, self).list(request,)


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    search_fields = ('medico', 'dia')

    def list(self, request):
        queryset = Agenda.objects.all()
        serializer = AgendaSerializer(queryset, many=True)
        return super(AgendaViewSet, self).list(request,)

