from django.db import models
from medico.models import Medico

# Create your models here.
class Horario(models.Model):
    horario = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'{self.horario}'


class Agenda(models.Model):
    """
    classe para a agenda do médico
    """
    id = models.AutoField(primary_key=True)
    medico = models.ForeignKey(
        Medico,
        verbose_name="Médico",
        on_delete=models.PROTECT,
        help_text='Selecione um médico')
    dia = models.DateField()
    horarios = models.ManyToManyField(
        Horario, verbose_name="horários",  help_text='Escolha os Horários')

    def get_horarios(self):
        return ", ".join([str(p) for p in self.horarios.all()])

    class Meta:
        unique_together = ('medico', 'dia')
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"

    def __unicode__(self):
        return f'medico: {self.medico}, dia: {self.dia}'
