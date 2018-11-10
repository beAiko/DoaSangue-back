from django.conf.urls import url
from .import views

urlpatterns = [
	url(r'^usuarios/$', views.UsuarioList.as_view(), name='usuario-list'),
	url(r'^doacoes/$', views.DoacaoList.as_view(), name='doacao-list'),
	url(r'^hemocentros/$', views.HemocentroList.as_view(), name='hemocentro-list'),
	url(r'^requisicoes/$', views.RequisicaoList.as_view(), name='requisicao-list'),

]
