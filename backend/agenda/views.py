from rest_framework import viewsets
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from agenda.models import Agenda
from medico.models import Medico
from agenda.models import Horario
from agenda.serializers import AgendaSerializer


# class AgendaFilter(filters.FilterSet):
#     medico = filters.ModelMultipleChoiceFilter(
#         queryset=Medico.objects.all())
#     # especialidade = filters.ModelMultipleChoiceFilter(
#     #     queryset=Especialidade.objects.all())

#     class Meta:
#         model = Agenda
#         fields = ['medico']



class AgendaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filter_class = AgendaFilter
    # filter_fields = '__all__'

    # def get_queryset(self):
    #     # Chances are, you're doing something more advanced here 
    #     # like filtering.
    #     Agenda.objects.all().order_by('date')

    # def list(self, request, *args, **kwargs):
    #     response = super().list(request, *args, **kwargs)
    #     qs = self.get_queryset()
    #     all_horarios = Horario.objects.filter(
    #         id__in=Agenda.horarios.through.objects.filter(
    #             agenda__in=qs
    #         ).values('horario_id')
    #     )
    #     horario_names = {}
    #     for horario in all_horarios:
    #         horario_names[horario.id] = horario.name

    #     categories_map = defaultdict(list)
    #     for m2m in agenda.categories.through.objects.filter(agenda__in=qs):
    #         categories_map[m2m.agenda_id].append(
    #             horario_names[m2m.horario_id]
    #         )

    #     for each in response.data:
    #         each['horarios'] = horarios_map.get(each['id'], [])

    #     return response

