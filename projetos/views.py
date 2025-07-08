from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Projeto, Atividade, Colaborador
from .serializers import ProjetoSerializer, AtividadeSerializer, ColaboradorSerializer
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def lista_projetos(request):
    projetos = Projeto.objects.filter(owner=request.user)
    return render(request, 'projetos/lista_projetos.html', {'projetos': projetos})

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Projeto.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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

def login_page(request):
    return render(request, 'projetos/login.html')