from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^carrinho/', include('carrinho.urls', namespace='carrinho')),  # Esta entrada deve aparecer antes da última
    # pois é mais restritiva.
    url(r'^', include('vendas.urls', namespace='vendas')),
]
