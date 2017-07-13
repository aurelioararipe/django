from django.shortcuts import render
from listaEmpresas.models import Empresa
# Create your views here.

def index(request):

	return render(request, 'index.html')

def exibir(request, empresa_id):
	print 'Id da empresa: %s' % (empresa_id)
	
	empresa = Empresa()
	if empresa_id == '1':
		empresa = Empresa('Menezes e Memorias', 'Rafael Franco', 'CE', 'Fortaleza', '8888888')

	if empresa_id == '2':
		empresa = Empresa('Menezes e HDs', 'Aurelio Araripe', 'CE', 'Ceara', '99999999')



	return render(request, 'listaEmpresas.html', {"empresa": empresa})
	
