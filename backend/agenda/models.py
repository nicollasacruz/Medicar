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
        on_delete=models.PROTECT,
        help_text='Selecione um médico')
    dia = models.DateField()
    horario = models.ManyToManyField(
        Horario, help_text='Escolha os Horários')

    def horarios(self):
        horarios = []
        for p in self.horario.all():
            horarios.append(p)
        return horarios 

    class Meta:
        unique_together = ('medico', 'dia')
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas"
        ordering = ['dia']

    def __str__(self):
        return f'{self.medico}'
