from rest_framework import serializers
from expander import ExpanderSerializerMixin
from consulta.models import Consulta
from especialidade.models import Especialidade
from medico.serializers import MedicoSerializer
from especialidade.serializers import EspecialidadeSerializer


class ConsultaSerializer(ExpanderSerializerMixin, serializers.Serializer):
    id = serializers.IntegerField()
    dia = serializers.DateField(required=False)
    horario = serializers.DateField(required=False)
    data_agendamento = serializers.DateTimeField(format="iso-8601", required=False, read_only=True)
    especialidade = serializers.SlugField()
    medico = serializers.SlugField()

    class Meta:
        model = Consulta
        fields = ('id', 'dia', 'horario', 'data_agendamento', 'especialidade', 'medico')
        expandable_fields = {
            'medico': MedicoSerializer,
            'especialidade': EspecialidadeSerializer
        }