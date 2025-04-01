from django.urls import path
from .views import ListarTarefa, CriarTarefa

urlpatterns = [
    path('', ListarTarefa.as_view(), name = 'listar_tarefas'),
    path('criar/', CriarTarefa.as_view(), name = 'criar_tarefa')
]