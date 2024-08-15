from django.urls import path
from .views import ProjectCreate, ProjectList, ProjectUpdate, task_list, nova_tarefa, edit_task, ProjectDetailView, ProjectDetail
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('projectadd', ProjectCreate.as_view(),  name='projectadd'),
    path('projectlist', ProjectList.as_view(), name='projectlist'),
    path('project/edit/<int:pk>/', ProjectUpdate.as_view(), name='projectedit'),
    path('task-list/', views.task_list, name='task_list'),
    path('tasks/new/', nova_tarefa, name='new_task'),
    path('tasks/edit/<int:task_id>/', edit_task, name='edit_task'),
    path('projects/detail/<int:pk>/', ProjectDetailView.as_view(), name='projectdetail'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='projectdetail'),
]
