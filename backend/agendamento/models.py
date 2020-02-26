from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Especialidade(models.Model):
    """
    Class Para definir as especilidades
    """
    id = models.AutoField(primary_key=True)
    nome = models.CharField(
        max_length=100, 
        unique=True,  
        help_text='Digite a especialidade')

    class Meta:
        verbose_name = "Especialidade"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.nome

class Medico(models.Model):
    """
    Class para definir os médicos
    """
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100, help_text='Digite a nome do médico')
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
        return self.nome

class Horarios(models.Model):
    horario = models.DateTimeField(auto_now=False, auto_now_add=False)


class Agenda(models.Model):
    """
    class para a agenda do médico
    """
    id = models.AutoField(primary_key=True)
    medico = models.ForeignKey(
        Medico,
        verbose_name="Médico", 
        on_delete=models.PROTECT,
        help_text='Selecione um médico')
    dia = models.DateField()

    class Meta:
        unique_together = ('medico', 'dia')
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas" 
        
    def __unicode__(self):
        return self.medico
        