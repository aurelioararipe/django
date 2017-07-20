from django.conf.urls import url
from listaEmpresas.views import index, exibir, convidar

urlpatterns = [
    # Examples:
    # url(r'^$', 'lojasAurafas.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index, name='index'),

    url(r'^listaEmpresas/(?P<empresa_id>\d+)$', exibir, name='exibir'),

    url(r'^listaEmpresas/(?P<empresa_id>\d+)/convidar$', convidar, name='convidar'),


]
