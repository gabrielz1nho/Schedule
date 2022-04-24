import email
from django.shortcuts import render
from django.contrib import messages
from django.core.validators import validate_email

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return render(request, 'accounts/logout.html')

def cadastro(request):
    if request.method != 'POST':
        return render(request, 'accounts/cadastro.html')
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('sobrenome')
    email = request.POST.get('email')
    usuario = request.POST.get('usuario')
    senha = request.POST.get('senha')
    senha2 = request.POST.get('senha2')

    if not nome or not sobrenome or not email or not usuario or not senha or not senha2:
        messages.error(request,'Nenhum campo pode estar vazio.')
        return render(request, 'accounts/cadastro.html')

    try:
        validate_email(email)
    except:
        messages.error(request,'Email inválido.')
        return render(request, 'accounts/cadastro.html')
    
    if len(senha) < 6:
        pass



def dashboard(request):
    return render(request, 'accounts/dashboard.html')