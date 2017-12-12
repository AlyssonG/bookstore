from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.detalhes_do_carrinho, name='detalhes_do_carrinho'),
    url(r'^adicionar/(?P<id_produto>\d+)/$', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    url(r'^remover/(?P<id_produto>\d+)/$', views.remover_do_carrinho, name='remover_do_carrinho'),
]
