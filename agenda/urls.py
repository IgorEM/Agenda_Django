"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('agenda', views.lista_eventos),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.evento_submit),
    # path('',views.index), #outra forma de redirecionar pra pagina inicia ser /Agenda
    path('',RedirectView.as_view(url='/agenda')),
    path('login/', views.login_user), #criando a rota login/ para redirecionar quando o usuario nao estiver logado
    path('login/submit',views.submit_login), #login/submit/ /no final indica get
    path('logout/', views.logout_user),


]
