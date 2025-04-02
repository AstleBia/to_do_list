from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
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

class AtualizarTarefa(UpdateView):
    model = Tarefa
    form_class = FormTarefa
    template_name = 'editar_tarefa.html'
    success_url = reverse_lazy('listar_tarefas')

class DeletarTarefa(DeleteView):
    model = Tarefa
    template_name = 'deletar_tarefa.html'
    success_url = reverse_lazy('listar_tarefas')

class DetalharTarefa(DetailView):
    model = Tarefa
    template_name = 'detalhar_tarefa.html'