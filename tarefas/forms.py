from django import forms
from .models import Tarefa

class FormTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo','descricao','concluido']

    titulo = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite o titulo da tarefa'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Digite a descricao da tarefa'}))