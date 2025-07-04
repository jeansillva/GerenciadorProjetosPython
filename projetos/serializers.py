from rest_framework import serializers
from .models import Projeto, Atividade, Colaborador

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ['id', 'nome', 'email']

class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atividade
        fields = ['id', 'nome', 'descricao', 'projeto', 'responsavel', 'concluida']

class ProjetoSerializer(serializers.ModelSerializer):
    atividades = AtividadeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'descricao', 'data_inicio', 'data_fim', 'atividades']