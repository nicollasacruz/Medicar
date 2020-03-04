from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter
from especialidade.models import Especialidade
from especialidade.serializers import EspecialidadeSerializer

# Create your views here.
class EspecialidadeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    search_fields = ('nome',)
