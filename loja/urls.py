from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('vendas.urls', namespace='vendas'))

    # http://localhost:8000  ==>  Exibirá a página de abertura do site que exibe a lista de produtos disponíveis
    # Não é preciso o url: http://localhost:8000/vendas
]
