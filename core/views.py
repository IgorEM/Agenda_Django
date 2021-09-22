from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento #importou a tabela
from django.contrib.auth.decorators import login_required #obrigar a está logado para ver a agenda
from django.contrib.auth import authenticate, login, logout #usado para autenticar e logar na função submit_login
from django.contrib import messages
# Create your views here.





# def index(request):
#     return redirect('/agenda') #outra forma de redirecionar pra pagina inicia ser /Agenda

def login_user(request):
   return render(request, 'login.html') #essa view carrega a template login.html


def logout_user(request):
    logout(request) #importei logout
    return redirect('/') #redireciona pro index

def submit_login(request):
    if request.POST: # se a requisição for do tipo post
        username = request.POST.get('username') #recebendo o username e password do forms
        password = request.POST.get('password')
        # agora temos que autenticar
        usuario = authenticate(username=username, password=password) #importei authenticate
        # agora temos que logar
        if usuario is not None: #se not None ele loga, se estiver tudo ok , e se não tiver?
            login(request, usuario) #importei login
            return redirect('/')
        else: # se não tiver tudo ok, usuario ou senha invalida
            messages.error(request, "Usuário ou Senha inválido")
    return redirect('/')


@login_required(login_url='/login/') #obrigar a está logado para ver a agenda # quando não estiver logado ele vai pra essa rota
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario) #objects.all() - select * # agora esta retornando uma lista
    dados = {'eventos': evento} #dicionario #dados
    return render(request, 'agenda.html', dados)

    # evento = Evento.objects.get(id=1) #consulta sql

    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)  # quando o campo usuario for igual a o usuario da requisição


# def retorna_local(request,titulo_evento):
#     consulta = Evento.objects.get(titulo=titulo_evento)
#     return HttpResponse('<h1>o local do evento é : {} <h1>'.format(consulta.data_criacao))

@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')


