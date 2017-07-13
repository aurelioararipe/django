from django.db import models


class Empresa(models.Model): 
	razao_social = models.CharField(max_length=255, null=False)
	proprietario = models.CharField(max_length=255, null=False)
	estado = models.CharField(max_length=255, null=False)
	cidade = models.CharField(max_length=255, null=False)
	telefone = models.CharField(max_length=15, null=False)