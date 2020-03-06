from rest_framework import serializers
from agenda.models import Agenda
from agenda.models import Horario
from medico.models import Medico
from medico.serializers import MedicoSerializer
from expander import ExpanderSerializerMixin
from django.conf import settings
from rest_framework.serializers import DateField


class HorarioSerializer(serializers.Serializer):
    horario = serializers.TimeField(format=settings.DATE_FORMAT)

    class Meta:
        model = Horario
        fields = ('horario')


class AgendaSerializer(ExpanderSerializerMixin, serializers.Serializer):
    id = serializers.IntegerField()
    dia = serializers.DateField(required=False)
    medico = serializers.SlugField()
    horarios = serializers.SlugField()

    class Meta:
        model = Agenda
        fields: ('id', 'dia' 'medico', 'horarios',)
        expandable_fields = {
            'medico': MedicoSerializer
        }
