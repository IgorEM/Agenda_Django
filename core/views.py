from django.shortcuts import render, HttpResponse
from core.models import Evento #importou a tabela
# Create your views here.

def lista_eventos(request):

    evento = Evento.objects.all() #objects.all() - select * # agora esta retornando uma lista
    dados = {'eventos': evento} #dicionario #dados
    return render(request, 'agenda.html', dados)

    # evento = Evento.objects.get(id=1) #consulta sql

    # usuario = request.user
    # evento = Evento.objects.filter(usuario=usuario)  # quando o campo usuario for igual a o usuario da requisição


# def retorna_local(request,titulo_evento):
#     consulta = Evento.objects.get(titulo=titulo_evento)
#     return HttpResponse('<h1>o local do evento é : {} <h1>'.format(consulta.data_criacao))