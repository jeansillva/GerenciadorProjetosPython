from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Projeto, Atividade, Colaborador
from .serializers import ProjetoSerializer, AtividadeSerializer, ColaboradorSerializer

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos/lista_projetos.html', {'projetos': projetos})

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]