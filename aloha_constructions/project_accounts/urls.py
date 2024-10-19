from django.urls import path
from . import views
from project_base.views import index  # Importando a view index de project_base
from . import views  # Supondo que você tenha outras views aqui

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Rota para logout
    path('', index, name='index'),  # Página inicial
]
