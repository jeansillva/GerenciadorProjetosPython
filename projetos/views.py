from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .atividade_form import AtividadeForm
from .colaborador_form import ColaboradorForm
from .models import Projeto, Atividade, Colaborador
from .projeto_form import ProjetoForm
from .serializers import ProjetoSerializer, AtividadeSerializer, ColaboradorSerializer

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', 'lista_projetos')
            return redirect(next_url)
        else:
            return render(request, 'projetos/login.html', {'error': 'Usuário ou senha inválidos'})

    return render(request, 'projetos/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def lista_projetos(request):
    projetos = Projeto.objects.filter(responsaveis=request.user)
    return render(request, 'projetos/lista_projetos.html', {'projetos': projetos})

@login_required
def detalhes_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id, responsaveis=request.user)
    return render(request, 'projetos/detalhes_projeto.html', {
        'projeto': projeto
    })

@login_required
def atividades_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id, responsaveis=request.user)
    atividades = projeto.atividades.all().order_by('-data_atualizacao')
    return render(request, 'projetos/atividades_projeto.html', {
        'projeto': projeto,
        'atividades': atividades
    })

@login_required
def criar_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.owner = request.user
            projeto.save()
            # Adiciona os responsáveis selecionados
            form.save_m2m()  # Necessário para salvar o campo ManyToMany
            # Garante que o criador também é um responsável
            projeto.responsaveis.add(request.user)
            return redirect('lista_projetos')
    else:
        form = ProjetoForm()

    return render(request, 'projetos/criar_projeto.html', {'form': form, 'titulo': 'Novo Projeto'})

@login_required
def editar_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id, responsaveis=request.user)

    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            form.save()
            return redirect('lista_projetos')
    else:
        form = ProjetoForm(instance=projeto)

    return render(request, 'projetos/criar_projeto.html', {
        'form': form,
        'titulo': 'Editar Projeto',
        'projeto': projeto
    })

@login_required
def remover_projeto(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)

    # Verifica se o usuário é o proprietário do projeto
    if request.user != projeto.owner:
        messages.error(request, 'Você não tem permissão para remover este projeto.')
        return redirect('lista_projetos')

    if request.method == 'POST':
        nome_projeto = projeto.nome
        projeto.delete()
        messages.success(request, f'Projeto "{nome_projeto}" foi removido com sucesso.')
        return redirect('lista_projetos')

    return render(request, 'projetos/confirmar_remover_projeto.html', {'projeto': projeto})

@login_required
def criar_atividade(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id, responsaveis=request.user)

    if request.method == 'POST':
        form = AtividadeForm(request.POST)
        if form.is_valid():
            atividade = form.save(commit=False)
            atividade.projeto = projeto
            atividade.save()
            return redirect('atividades_projeto', projeto_id=projeto.id)
    else:
        form = AtividadeForm()

    return render(request, 'projetos/atividade_form.html', {
        'form': form,
        'projeto': projeto,
        'titulo': 'Nova Atividade'
    })

@login_required
def editar_atividade(request, atividade_id):
    atividade = get_object_or_404(Atividade, id=atividade_id, projeto__responsaveis=request.user)

    if request.method == 'POST':
        form = AtividadeForm(request.POST, instance=atividade)
        if form.is_valid():
            form.save()
            return redirect('atividades_projeto', projeto_id=atividade.projeto.id)
    else:
        form = AtividadeForm(instance=atividade)

    return render(request, 'projetos/atividade_form.html', {
        'form': form,
        'atividade': atividade,
        'projeto': atividade.projeto,
        'titulo': 'Editar Atividade'
    })

@login_required
def toggle_atividade(request, atividade_id):
    if request.method == 'POST':
        atividade = get_object_or_404(Atividade, id=atividade_id, projeto__responsaveis=request.user)
        atividade.concluida = not atividade.concluida
        atividade.save()
    return redirect('atividades_projeto', projeto_id=atividade.projeto.id)

@login_required
def lista_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'projetos/lista_colaboradores.html', {'colaboradores': colaboradores})

@login_required
def criar_colaborador(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador cadastrado com sucesso!')
            return redirect('lista_colaboradores')
    else:
        form = ColaboradorForm()

    return render(request, 'projetos/colaborador_form.html', {
        'form': form,
        'titulo': 'Novo Colaborador'
    })

@login_required
def editar_colaborador(request, colaborador_id):
    colaborador = get_object_or_404(Colaborador, id=colaborador_id)

    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador atualizado com sucesso!')
            return redirect('lista_colaboradores')
    else:
        form = ColaboradorForm(instance=colaborador)

    return render(request, 'projetos/colaborador_form.html', {
        'form': form,
        'titulo': 'Editar Colaborador',
        'colaborador': colaborador
    })

@login_required
def remover_colaborador(request, colaborador_id):
    if request.method == 'POST':
        colaborador = get_object_or_404(Colaborador, id=colaborador_id)
        nome_colaborador = colaborador.nome
        colaborador.delete()
        messages.success(request, f'Colaborador "{nome_colaborador}" removido com sucesso!')
        return redirect('lista_colaboradores')
    return redirect('lista_colaboradores')

class ProjetoViewSet(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Projeto.objects.filter(responsaveis=self.request.user)

    def perform_create(self, serializer):
        projeto = serializer.save(owner=self.request.user)
        projeto.responsaveis.add(self.request.user)

class AtividadeViewSet(viewsets.ModelViewSet):
    queryset = Atividade.objects.all()
    serializer_class = AtividadeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Atividade.objects.filter(projeto__responsaveis=self.request.user)

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Colaborador.objects.all()
