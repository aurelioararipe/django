from django.db import models

# Create your models here.

class Empresa(object):
	def __init__(self, razao_social="", proprietario="", estado="", cidade="", telefone=""):
		self.razao_social = razao_social
		self.proprietario = proprietario
		self.estado = estado
		self.cidade = cidade
		self.telefone = telefone