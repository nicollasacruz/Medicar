from rest_framework import serializers
from especialidade.models import Especialidade


class EspecialidadeSerializer(serializers.HyperlinkedModelSerializer):
    url_field_name = 'url'

    class Meta:
        model = Especialidade
        fields = ('url', 'id', 'nome')
        