from django.shortcuts import render
from .models import Projeto

def lista_projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos/lista_projetos.html', {'projetos': projetos})

