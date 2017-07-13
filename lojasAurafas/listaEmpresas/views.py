from django.shortcuts import render
from listaEmpresas.models import Empresa
# Create your views here.

def index(request):

	return render(request, 'index.html', {'empresas': Empresa.objects.all()})

def exibir(request, empresa_id):
	print 'Id da empresa: %s' % (empresa_id)
	
	empresa = Empresa.objects.get(id=empresa_id)


	return render(request, 'listaEmpresas.html', {"empresa": empresa})
	
