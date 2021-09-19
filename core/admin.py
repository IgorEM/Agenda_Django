from django.contrib import admin
from core.models import Evento
# Register your models here.
#Registrando o modelo Evento criado

class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuario','data_evento',)

admin.site.register(Evento, EventoAdmin) #essa classe registra essa classe aqui