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
        fields = ['text', 'completed', 'estimated_time']  # O campo está correto?
        widgets = {
            'estimated_time': forms.TextInput(attrs={
                'placeholder': 'HH:MM', 
                'id': 'id_estimated_time'  # Certifique-se de que o ID está correto
            }),
        }
        