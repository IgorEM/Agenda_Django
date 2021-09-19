from django.db import models
from django.contrib.auth.models import User
#python manage.py makemigrations core
#python manage.py sqlmigrate core 0001
#python manage.py migrate core 0001

# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length = 100)
    descricao = models.TextField(blank = True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)

    class Meta: #metadados da tabela, forçando o nome da tabela core_evento se tornar evento
        db_table = 'evento'

    def __str__(self): #agora o evento aparece como object 1
        return self.titulo
