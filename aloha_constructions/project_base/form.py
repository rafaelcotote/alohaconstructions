from django import forms
from project_base.models import CadastroProjeto
from project_base.models import Task


class CadastroProjetoForm(forms.ModelForm):
    class Meta:
        model = CadastroProjeto
        fields = ('project_name', 'project_description', 'client_name', 'project_adress', 'estimated_budget', 'total_amount_spend', 'estimated_project_duration')

class ProjectFilterForm(forms.Form):
    project_name = forms.CharField(required=False, label='Project Name')
    client_name = forms.CharField(required=False, label='Client Name')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['text', 'completed', 'estimated_time']
        widgets = {
            'time_estimate': forms.TextInput(attrs={'placeholder': 'HH:MM'}),
        }
        