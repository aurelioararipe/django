from django.shortcuts import render
from listaEmpresas.models import Empresa
from django.shortcuts import redirect
# Create your views here.

def index(request):

	return render(request, 'index.html', {'empresas': Empresa.objects.all()})

def exibir(request, empresa_id):
	print 'Id da empresa: %s' % (empresa_id)
	
	empresa = Empresa.objects.get(id=empresa_id)


	return render(request, 'listaEmpresas.html', {"empresa": empresa})
	
def convidar(request, empresa_id):
	empresa_a_convidar = Empresa.objects.get(id=empresa_id)
	empresa_logado = get_empresa_logado(request)
	empresa_logado.convidar(empresa_a_convidar)
	return redirect('index')


def get_empresa_logado(request):
	return Empresa.objects.get(id=1)