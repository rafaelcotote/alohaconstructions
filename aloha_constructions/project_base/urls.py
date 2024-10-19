from django.urls import path
from . import views
from .views import delete_task

urlpatterns = [
    path('', views.index, name='index'),
    path('projectadd/', views.ProjectCreate.as_view(), name='projectadd'),
    path('projectlist/', views.ProjectList.as_view(), name='projectlist'),
    path('project/edit/<int:pk>/', views.ProjectUpdate.as_view(), name='projectedit'),
    path('task-list/', views.task_list, name='task_list'),
    path('tasks/new/', views.nova_tarefa, name='new_task'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('projects/detail/<int:pk>/', views.ProjectDetailView.as_view(), name='projectdetail'),  # Escolha apenas uma dessas linhas
    path('tasks/delete/<int:task_id>/', delete_task, name='delete_task'),
    
]
