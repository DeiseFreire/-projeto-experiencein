# experiencein/perfis/models.py
# logo abaixo da declaração da classe Perfil
class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE)
