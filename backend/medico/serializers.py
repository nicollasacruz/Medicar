from rest_framework import serializers
from medico.models import Medico
from especialidade.serializers import EspecialidadeSerializer
from expander import ExpanderSerializerMixin


class MedicoSerializer(ExpanderSerializerMixin, serializers.HyperlinkedModelSerializer):
    url_field_name = 'url'

    class Meta:
        model = Medico
        fields = '__all__'
        expandable_fields = {
            'especialidade': EspecialidadeSerializer
        }