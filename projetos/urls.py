from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_views
from . import views

router = DefaultRouter()
router.register(r'projetos', views.ProjetoViewSet)
router.register(r'atividades', views.AtividadeViewSet)
router.register(r'colaboradores', views.ColaboradorViewSet)
urlpatterns = [
    path('', views.login_page, name='login'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('projetos/', views.lista_projetos, name='lista_projetos'),
    path('projetos/criar/', views.criar_projeto, name='criar_projeto'),
    path('projetos/<int:projeto_id>/', views.detalhes_projeto, name='detalhes_projeto'),
    path('projetos/<int:projeto_id>/editar/', views.editar_projeto, name='editar_projeto'),
    path('projetos/<int:projeto_id>/remover/', views.remover_projeto, name='remover_projeto'),

    path('projetos/<int:projeto_id>/atividades/', views.atividades_projeto, name='atividades_projeto'),
    path('projetos/<int:projeto_id>/atividades/criar/', views.criar_atividade, name='criar_atividade'),
    path('atividades/<int:atividade_id>/editar/', views.editar_atividade, name='editar_atividade'),
    path('atividades/<int:atividade_id>/toggle/', views.toggle_atividade, name='toggle_atividade'),

    path('colaboradores/', views.lista_colaboradores, name='lista_colaboradores'),
    path('colaboradores/criar/', views.criar_colaborador, name='criar_colaborador'),
    path('colaboradores/<int:colaborador_id>/editar/', views.editar_colaborador, name='editar_colaborador'),
    path('colaboradores/<int:colaborador_id>/remover/', views.remover_colaborador, name='remover_colaborador'),

    path('api/', include(router.urls)),
    path('api-token-auth/', token_views.obtain_auth_token, name='api-token'),
]

