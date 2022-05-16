# experiencein/perfis/models.py

from django.db import models

class Perfil(models.Model):
    def __init__(self, nome='', email='', telefone= '', nome_empresa=''):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.nome_empresa = nome_empresa