from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')  # Redireciona para a página inicial ou outra página
        else:
            messages.error(request, 'Credenciais inválidas.')
    
    return render(request, 'login.html')  # Renderiza a página de login

def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login


@login_required
def home(request):
    return render(request, 'index.html')  # Crie um template home.html

# Create your views here.

