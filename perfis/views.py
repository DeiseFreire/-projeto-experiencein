# experiencein/perfis/views.py
from django.shortcuts import render
from perfis.models import Perfil
# código comentado
def get_perfil_logado(request):
   return Perfil.objects.get(id=1) 
   # [IMPORTANTE]: Trocar o ID por um que esteja cadastrado 
