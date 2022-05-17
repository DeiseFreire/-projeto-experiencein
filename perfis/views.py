# experiencein/perfis/views.py
from django.shortcuts import render
from perfis.models import Perfil
# código comentado
# modificando a função convidar
def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return render(request, 'index.html', {'perfis' : Perfil.objects.all()})
def get_perfil_logado(request):
    return Perfil.objects.get(id=1)