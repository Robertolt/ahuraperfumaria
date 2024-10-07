from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from rolepermissions.decorators import has_permission_decorator 
from django.contrib import auth


def index(request):
    return render(request,'initialpage/index.html')

def redirect_to_app_gestao(request):
    if request.method == 'POST':
        return redirect(reverse('gestao'))  # Redireciona para a app blog
    else:
        return render(request, 'initialpage/index.html')
    
@has_permission_decorator('login')
def areadogerente(request):
    if request.method == 'GET':
        return render(request, 'initialpage/areadogerente.html')
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
    
def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(reverse('index'))
        return render(request, 'initialpage/login.html')
    elif request.method == 'POST':
        login = request.POST.get('nome')
        senha = request.POST.get('senha')

    user = auth.authenticate(username=login, password=senha)

    if not user:
        return HttpResponse('Usuário inválido')
    
    auth.login(request, user)
    return HttpResponse('Usuário logado com sucesso')


def sair(request):
    request.session.flush()
    return redirect(reverse('login'))