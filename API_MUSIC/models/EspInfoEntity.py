from django.db import models
from django.utils import timezone

class EspInfoEntity(models.Model):
    data = models.DateField(auto_now_add=True)
    tempo_de_estudo = models.FloatField(default=0.0)  # Tempo de estudo em horas iniciado como zero
    ultima_atualizacao = models.DateTimeField(auto_now=True)  # Campo para registrar a última atualização

    def __str__(self):
        return f"Estudo em {self.data}"
