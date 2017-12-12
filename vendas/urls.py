from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_produtos, name='lista_produtos'),
    url(r'^(?P<slug_da_categoria>[-\w]+)/$', views.lista_produtos, name='lista_produtos_por_categoria'),
    url(r'^(?P<id>\d+)/(?P<slug_do_produto>[-\w]+)/$', views.exibe_produto, name='exibe_produto'),

]
