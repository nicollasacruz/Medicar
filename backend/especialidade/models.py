from django.db import models

# Create your models here.
class Especialidade(models.Model):
    """
    Classe Para definir as especilidades
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
