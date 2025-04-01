from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Tarefa
from .forms import FormTarefa
from django.urls import reverse_lazy
# Create your views here.

class ListarTarefa(ListView):
    model = Tarefa
    template_name = 'listar_tarefas.html'
    context_object_name = 'tarefas'

class CriarTarefa(CreateView):
    model = Tarefa
    form_class = FormTarefa
    template_name = 'criar_tarefa.html'
    success_url = reverse_lazy('listar_tarefas')