from django.db import models
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse


class Menu(models.Model):
    texto = models.CharField(max_length=20, db_index=True)
    ref = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ('texto',)

    def __str__(self):
        return self.texto


class Tabela(models.Model):
    titulo = models.CharField(max_length=20, db_index=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.titulo


class Rodape(models.Model):
    titulo = models.CharField(max_length=20, db_index=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return self.titulo


class Carousel(models.Model):
    imagem = models.TextField(blank=True)

    class Meta:
        ordering = ('imagem',)

    def __str__(self):
        return self.imagem


class Descricao(models.Model):
    texto = models.CharField(max_length=200, db_index=True)
    size = models.CharField(max_length=3)

    class Meta:
        ordering = ('size',)

    def __str__(self):
        return self.texto


class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def get_absolute_path(self):
        return reverse('vendas:lista_produtos_por_categoria', args=[self.slug])

    def __str__(self):
        return self.nome


# url(r'^(?P<slug_da_categoria>[-\w]+)/$', views.lista_produtos, name='lista_produtos_por_categoria'),
# /computador/
# /celular/
# /eletrodomestico/

# ?	- zero ou um do elemento anterior.
# *	- zero ou mais do elemento anterior.
# +	- um ou mais do elemento anterior.
# \w - para encontrar um word character. Um word character é um caracter de a-z, A-Z, 0-9, e _ (underscore).

# from shop.models import Produto
# c = Categoria.objects.get(id=1)
# c.get_absolute_path()
# '/computador/'

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos')
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagem = models.TextField(blank=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)
    data_cadastramento = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    botao = models.CharField(max_length=10, db_index=True, default="Comprar")

    class Meta:
        ordering = ('-data_cadastramento',)

    def cadastrado_recentemente(self):
        return self.data_cadastramento >= timezone.now() - datetime.timedelta(days=1)

    def get_absolute_path(self):
        return reverse('vendas:exibe_produto', args=[self.id, self.slug])

    def __str__(self):
        return self.nome

# url(r'^(?P<id>\d+)/(?P<slug_do_produto>[-\w]+)/$', views.exibe_produto, name='exibe_produto'),
# /5/smartphone-samsung-galaxy-s8-plus/
# /4/smartphone-samsung-galaxy-s8/
# /2/computador-com-monitor-led-19-5-easypc-intel-core-i5-8gb-hd-1tb/

# ?	- zero ou um do elemento anterior.
# *	- zero ou mais do elemento anterior.
# +	- um ou mais do elemento anterior.
# \w - para encontrar um word character. Um word character é um caracter de a-z, A-Z, 0-9, e _ (underscore).

# from shop.models import Produto
# produto = Produto.objects.get(id=1)
# produto.get_absolute_path()
# '/1/notebook-del-vostro-3458-i3/'
