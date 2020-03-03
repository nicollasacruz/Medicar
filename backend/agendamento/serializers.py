from rest_framework import serializers
from agendamento.models import Especialidade
from agendamento.models import Medico
from agendamento.models import Agenda
from expander import ExpanderSerializerMixin


class EspecialidadeSerializer(serializers.HyperlinkedModelSerializer):
    url_field_name = 'url'

    class Meta:
        model = Especialidade
        fields = ('url', 'id', 'nome')


class MedicoSerializer(ExpanderSerializerMixin, serializers.HyperlinkedModelSerializer):
    url_field_name = 'url'

    class Meta:
        model = Medico
        fields = ('url', 'id', 'crm', 'nome', 'especialidade')
        expandable_fields = {
            'especialidade': EspecialidadeSerializer
        }


class AgendaSerializer(ExpanderSerializerMixin, serializers.HyperlinkedModelSerializer):
    url_field_name = 'url'

    class Meta:
        model = Agenda
        fields:('url', 'id', 'medico', 'get_horarios')
        expandable_fields = {
            'medico': MedicoSerializer
        }
