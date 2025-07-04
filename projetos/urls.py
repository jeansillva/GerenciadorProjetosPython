from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as token_views
from . import views

router = DefaultRouter()
router.register(r'projetos', views.ProjetoViewSet)
router.register(r'atividades', views.AtividadeViewSet)
router.register(r'colaboradores', views.ColaboradorViewSet)

urlpatterns = [
    path('', views.lista_projetos, name='lista_projetos'),
    path('api/', include(router.urls)),
    path('api-token-auth/', token_views.obtain_auth_token, name='api-token'),
]