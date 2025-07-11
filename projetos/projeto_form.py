from django import forms
from django.contrib.auth.models import User
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    responsaveis = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = Projeto
        fields = ['nome', 'descricao', 'data_inicio', 'data_fim', 'responsaveis']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'data_inicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_fim': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
