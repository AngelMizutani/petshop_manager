from django.views.generic import TemplateView
from .models import Cidade, Pessoa
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class Index(TemplateView):
    template_name = 'paginas/index.html'

class CidadeCreate(CreateView):
    model = Cidade
    fields = ['nome', 'estado']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')

class PessoaCreate(CreateView):
    model = Pessoa
    fields = ['nome', 'nascimento', 'email', 'cidade']
    template_name = 'cadastros/formulario.html'
    success_url = reverse_lazy('index')
 