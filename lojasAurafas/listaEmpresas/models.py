from django.db import models


class Empresa(models.Model): 
	razao_social = models.CharField(max_length=255, null=False)
	proprietario = models.CharField(max_length=255, null=False)
	estado = models.CharField(max_length=255, null=False)
	cidade = models.CharField(max_length=255, null=False)
	telefone = models.CharField(max_length=15, null=False)
	def convidar(self, empresa_convidado):
		Convite(solicitante=self, convidado=empresa_convidado).save()

class Convite(models.Model):
	solicitante = models.ForeignKey(Empresa, related_name='convites_feitos')
	convidado = models.ForeignKey(Empresa, related_name='convites_recebidos')	

	