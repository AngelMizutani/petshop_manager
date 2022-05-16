from django.urls import path
from .views import Index, CidadeCreate, PessoaCreate

urlpatterns = [
    # path('inicio/', Index.as_view(), name='index'),
    path('', Index.as_view(), name='index'),
    path('cadastrar/cidade/', CidadeCreate.as_view(), name="cadastrar-cidade"),
    path('cadastrar/pessoa/', PessoaCreate.as_view(), name="cadastrar-pessoa"),
]
