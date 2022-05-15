"""experiencein Configuração de URL

A lista `urlpatterns` encaminha URLs para visualizações. Para mais informações consulte:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examplos:
Visualizações de funções
    1. Adicionar uma importação:  from my_app import views
    2. Adicionar um URL aos urlpatterns:  path('', views.home, name='home')
Visualizações baseadas em classe
    1. Adicionar uma importação:  from other_app.views import Home
    2. Adicionar um URL aos urlpatterns:  path('', Home.as_view(), name='home')
Incluindo outro URLconf
    1. Importe a função include(): from django.urls import include, path
    2. Adicionar um URL aos urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from perfis import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('perfis.urls')),
    path('', include('usuarios.urls'))
]