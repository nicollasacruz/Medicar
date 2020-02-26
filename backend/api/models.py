from django.db import models

# Create your models here.
class Especialidade(models.Model):
    """
    Class Para definir as especilidades
    """
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Especialidade"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.nome


class Medico(models.Model):
    """
    Class para os Medicos 
    """
    nome = models.CharField(max_length=100)
    crm = models.IntegerField()
    email = models.EmailField()
    telefone = models.IntegerField()
    especialidade = models.ForeignKey(Especialidade, verbose_name="Especialidade", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"  

    def __str__(self):
        return self.nome


class Agenda(models.Model):
    """
    Class para o agendamento dos clientes
    """
    medico = models.ForeignKey(Medico, verbose_name="Medico", on_delete=models.PROTECT)
    dia = models.DateField()
    horarios = models.DateTimeField()

    class Meta:
        verbose_name = "Agenda"
        verbose_name_plural = "Agendas" 

    def __str__(self):
        return self.dia

    def agendar(self):
        pass


class Consuta(models.Model):
    """
    Class Para as consultas marcadas
    """
    pass

