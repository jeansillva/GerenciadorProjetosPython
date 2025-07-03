from django.contrib import admin
from .models import Projeto, Atividade, Colaborador

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
    search_fields = ('nome', 'email')

@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'data_fim')
    search_fields = ('nome',)
    list_filter = ('data_inicio',)

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'projeto', 'responsavel', 'concluida')
    search_fields = ('nome', 'projeto__nome', 'responsavel__nome')
    list_filter = ('concluida', 'projeto')
