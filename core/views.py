from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento #importou a tabela
from django.contrib.auth.decorators import login_required #obrigar a está logado para ver a agenda
from django.contrib.auth import authenticate, login, logout #usado para autenticar e logar na função submit_login
from django.contrib import messages
from django.http.response import Http404,JsonResponse
from datetime import datetime, timedelta
# Create your views here.





# def index(request):
#     return redirect('/agenda') #outra forma de redirecionar pra pagina inicia ser /Agenda

def login_user(request):
   return render(request, 'login.html') #essa view carrega a template login.html


def logout_user(request):
    logout(request) #importei logout
    return redirect('/') #redireciona pro index

@login_required(login_url='/login/')
def evento_submit(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:#se existir id, é pq estamos alterando um evento
            evento = Evento.objects.get(id=id_evento) #pegou evento pelo id
            if evento.usuario == usuario: #se o usuario logado for igual a o que quer fazer a  alteração
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save()
            #outra forma sem verificar o usuario->>> Evento.objects.filter(id=id_evento).update(titulo=titulo,data_evento=data_evento,descricao=descricao)

        else: #se não existir estamos criando
        #temos que registrar agora
            Evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario)
        return redirect('/')



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
    #data_atual = datetime.now() - timedelta(hours=1)
    evento = Evento.objects.filter(usuario=usuario)
                                   #data_evento__gt=data_atual) #objects.all() - select * # agora esta retornando uma lista
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
    id_evento = request.GET.get('id') #estamos pegando o id da url de eventos
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento) #armazenando os dados do evento de tal id . para poder retornar na edição(template evento.html)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=id_evento) #filtrando por id e passando o parametro
    except Exception:
        raise Http404
    if usuario == evento.usuario:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')


#renderizando #lista no formato formato JsonResponse #
@login_required(login_url='/login/')
def json_lista_evento(request,id_usuario): #pra pegar de acordo com o id daquele usuario
    usuario = User.objects.get(id=id_usuario)
    evento = Evento.objects.filter(usuario=usuario).values('id','titulo','descricao','data_evento','usuario')
    return JsonResponse(list(evento), safe=False)