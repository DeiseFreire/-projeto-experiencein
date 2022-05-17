# experiencein/perfis/models.py
# logo abaixo da declaração da classe Perfil
class Convite(models.Model):
   solicitante = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_feitos')
   convidado = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name='convites_recebidos')