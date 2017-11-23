from django.conf.urls import url
from . import views

urlpatterns = [
    # Esta primeira view tem por objetivo listar todos os produtos
    # O URLconf abaixo trata requisições para http://localhost:8000
    url(r'^$', views.lista_produtos, name='lista_produtos'),

    # E esta view é utilizada para listar os produtos de uma determinada categoria
    # E este URLconf trata requisições para http://localhost:8000/computador/
    url(r'^(?P<slug_da_categoria>[-\w]+)/$', views.lista_produtos, name='lista_produtos_por_categoria'),

    # Esta view é utilizada para exibir um determinado produto
    # Este URLconf trata requisições para http://localhost:8000/6/smartphone-samsung-galaxy-s8-plus/
    url(r'^(?P<id>\d+)/(?P<slug_do_produto>[-\w]+)/$', views.exibe_produto, name='exibe_produto'),

    # ?	 - zero ou um do elemento anterior.
    # *	 - zero ou mais do elemento anterior.
    # +	 - um ou mais do elemento anterior.
    # \w - para encontrar um word character. Um word character é um caracter de a-z, A-Z, 0-9, e _ (underscore).
]
