from django.urls import path
from .views import ListarTarefa, CriarTarefa, AtualizarTarefa, DeletarTarefa, DetalharTarefa

urlpatterns = [
    path('', ListarTarefa.as_view(), name = 'listar_tarefas'),
    path('criar/', CriarTarefa.as_view(), name = 'criar_tarefa'),
    path('editar/<int:pk>', AtualizarTarefa.as_view(), name = 'editar_tarefa'),
    path('deletar/<int:pk>', DeletarTarefa.as_view(), name = 'deletar_tarefa'),
    path('detalhar/<int:pk>',DetalharTarefa.as_view(), name='detalhar_tarefa')
]