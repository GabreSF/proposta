from django.db import models

class Proposta(models.Model):
    document = models.CharField(max_length=50) 
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    descricao = models.TextField()
    aprovada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
