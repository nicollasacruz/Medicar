from django.db import models
from especialidade.models import Especialidade
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Medico(models.Model):
    """
    Classe para definir os médicos
    """
    id = models.AutoField(primary_key=True)
    nome = models.CharField(
        max_length=100, help_text='Digite a nome do médico')
    crm = models.CharField(unique=True, max_length=7,
                           help_text='Digite o CRM do médico')
    email = models.EmailField(help_text='Digite o E-mail do médico',
                              verbose_name="E-mail")
    telefone = PhoneNumberField(
        blank=True, help_text='Digite o telefone do médico')
    especialidade = models.ForeignKey(
        Especialidade,
        on_delete=models.PROTECT,
        help_text='Selecione a especialidade do médico')

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"

    def __str__(self):
        return f'{self.nome}'
