from django.db import models

# Create your models here.
class Consulta(models.Model):
    agenda = models.ForeignKey()
    horario = models.ForeignKey('TargetModel', related_name='', on_delete=models.CASCADE)
