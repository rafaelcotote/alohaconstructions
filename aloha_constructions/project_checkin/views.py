from django.shortcuts import render, redirect
from .forms import CheckinRegisterForm
from django.views.generic import ListView
from .models import CheckinRegister
from django.contrib.auth.models import User  # Importe o modelo User do Django
from project_base.models import CadastroProjeto
from project_client.models import Client
from django.utils import timezone
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

def checkin_register(request):
    if request.method == 'POST':
        form = CheckinRegisterForm(request.POST, user=request.user)  # Passa o usuário logado para o formulário
        if form.is_valid():
            form.save()
            return redirect('checkin_success')
    else:
        form = CheckinRegisterForm(user=request.user)  # Passa o usuário logado para o formulário
    return render(request, 'checkin_register.html', {'form': form})

def checkin_success(request):
    return render(request, 'checkin_success.html')

class CheckinListView(ListView):
    model = CheckinRegister
    template_name = 'checkin_list.html'
    context_object_name = 'checkin_registers'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrar por employee
        employee_id = self.request.GET.get('employee')
        if employee_id:
            queryset = queryset.filter(employee_id=employee_id)

        # Filtrar por project
        project_id = self.request.GET.get('project')
        if project_id:
            queryset = queryset.filter(project_id=project_id)

        # Filtrar por activity
        activity_id = self.request.GET.get('activity')
        if activity_id:
            queryset = queryset.filter(activity_id=activity_id)

        # Filtrar por data_register
        date_register = self.request.GET.get('date_register')
        if date_register:
            date_register = timezone.datetime.strptime(date_register, '%Y-%m-%d').date()
            queryset = queryset.filter(date_register__date=date_register)

        # Filtrar por type_register
        type_register = self.request.GET.get('type_register')
        if type_register:
            queryset = queryset.filter(type_register=type_register)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all()  # Obtenha todos os usuários
        context['projects'] = CadastroProjeto.objects.all()
        context['clients'] = Client.objects.all()  # Supondo que você tenha um modelo de Project
        return context

# Create your views here.

def CheckinRegister(request):
    return render(request, 'adminlte/index.html', {})

