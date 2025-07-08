from django.db import models
from django.contrib.auth.models import User

class Colaborador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Atividade(models.Model):
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name='atividades')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    responsavel = models.ForeignKey(Colaborador, on_delete=models.SET_NULL, null=True, blank=True)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nome} ({'Concluída' if self.concluida else 'Pendente'})"
