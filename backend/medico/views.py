from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from medico.models import Medico
from medico.serializers import MedicoSerializer


class MedicoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    search_fields = ('nome',)
    