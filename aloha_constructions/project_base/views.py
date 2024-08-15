from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from .models import CadastroProjeto
from .form import CadastroProjetoForm
from .form import ProjectFilterForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Task
from .form import TaskForm

#CreateView

class ProjectCreate(CreateView):
    login_url = reverse_lazy('login')
    model = CadastroProjeto
    fields = ['project_name', 'project_description', 'client_name', 'project_adress', 'estimated_budget', 'total_amount_spend', 'estimated_project_duration']
    template_name = 'adminlte/project-add.html'
    #success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.usuario = self.request.user

        return super().form_valid(form)

    def get_success_url(self):
        # Redireciona para a mesma página com um parâmetro de consulta de sucesso
        return reverse_lazy('projectadd') + '?success=true'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['titulo'] = "Cadastro de Fornecedor"
        context['botao'] = "Create"

        return context

################UPDATE VIEW###############

class ProjectUpdate(UpdateView):
    model = CadastroProjeto
    form_class = CadastroProjetoForm
    template_name = 'adminlte/project_edit.html'
    context_object_name = 'project'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('projectedit', kwargs={'pk': self.object.pk}) + '?success=true'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Edit Project"
        context['botao'] = "Save Changes"
        return context

################READ VIEW############### 

class ProjectDetailView(DetailView):
    model = CadastroProjeto
    template_name = 'adminlte/project-detail.html'
    context_object_name = 'projeto'

################LIST VIEW###############    

class ProjectList(ListView):
    model = CadastroProjeto
    template_name = 'adminlte/project-list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = ProjectFilterForm(self.request.GET)
        if form.is_valid():
            project_name = form.cleaned_data.get('project_name')
            client_name = form.cleaned_data.get('client_name')
            if project_name:
                queryset = queryset.filter(project_name__icontains=project_name)
            if client_name:
                queryset = queryset.filter(client_name__name__icontains=client_name)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProjectFilterForm(self.request.GET)
        return context

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'adminlte/task_list.html', {'tasks': tasks})

def nova_tarefa(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'adminlte/new_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'adminlte/edit_task.html', {'form': form, 'task': task})

def index(request):
    quantidade_registros = CadastroProjeto.objects.count()
    quantidade_usuarios = User.objects.count()
    return render(request, 'adminlte/index.html', {'quantidade_registros': quantidade_registros, 'quantidade_usuarios': quantidade_usuarios})

def projectadd(request):
    return render(request, 'adminlte/project-add.html', {})

def projectlist(request):
    return render(request, 'adminlte/project-list.html', {})

class ProjectDetail(DetailView):
    model = CadastroProjeto
    template_name = 'adminlte/project-detail.html'
    context_object_name = 'project'

class ProjectUpdate(UpdateView):
    model = CadastroProjeto
    form_class = CadastroProjetoForm
    template_name = 'adminlte/project_edit.html'

    def get_success_url(self):
        return reverse_lazy('projectedit', kwargs={'pk': self.object.pk}) + '?success=true'

