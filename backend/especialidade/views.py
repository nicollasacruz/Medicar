from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from especialidade.models import Especialidade
from especialidade.serializers import EspecialidadeSerializer

# Create your views here.
class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    search_fields = ('nome',)

    def list(self, request):
        queryset = Especialidade.objects.all()
        serializer = EspecialidadeSerializer(queryset, many=True)
        return super(EspecialidadeViewSet, self).list(request,)
