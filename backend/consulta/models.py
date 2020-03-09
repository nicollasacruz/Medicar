from django.db import models
from especialidade.models import Especialidade
from medico.models import Medico
from agenda.models import Agenda
from django.utils import timezone

# Create your models here.
class Consulta(models.Model):
    """
    Classe para definir as consultas
    """
    id = models.AutoField(primary_key=True)
    dia = models.DateField()
    horario = models.TimeField(verbose_name='horário')
    data_agendamento = models.DateTimeField(
        auto_now_add=True, verbose_name='data de agandamento')
    especialidade = models.ForeignKey(Especialidade,
        on_delete=models.PROTECT,
        help_text='Selecione a especialidade para consulta')
    medico = models.ForeignKey(Medico,
        verbose_name='Médico',
        on_delete=models.PROTECT,
        help_text='Selecione um médico para a consulta')

    class Meta:
        verbose_name = "consulta"
        verbose_name_plural = "consultas"

    def __str__(self):
        return f'agendado horário {self.horario}, para o dia:{self.dia}'

