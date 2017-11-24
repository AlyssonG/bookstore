from django.shortcuts import render, get_object_or_404
from .models import Categoria, Produto, Menu, Carousel, Descricao, Tabela, Rodape


def lista_produtos(request, slug_da_categoria=None):
    categoria = None
    categorias = Categoria.objects.all()
    produtos = Produto.objects.filter(disponivel=True)
    if slug_da_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_da_categoria)
        produtos = produtos.filter(categoria=categoria)

    return render(request, 'vendas/produto/lista.html', {'categorias': categorias,
                                                         'produtos': produtos,
                                                         'categoria': categoria,
                                                         'menu' : get_menu_categorias(),
                                                         'carousel' : get_carousel(),
                                                         'descricao': get_descricao(),
                                                         'comment': get_rodape(),
                                                         'tabela': get_tabela()})


def exibe_produto(request, id, slug_do_produto):
    # Esta view espera receber o id do produto e seu slug para recuperar o produto
    # Podemos recuperar o produto apenas com o seu id uma vez que ele é unique.
    # Incluímos o slug para podermos construir 'SEO friendly URLs'.
    # SEO = Search Engine Optimization.
    # Exemplo: http://www.dominio.com.br/produto?id=721 <== Ruim
    # Exemplo: http://www.dominio.com.br/721/notebook-del-vostro-3458-i3 <== Bom
    produto = get_object_or_404(Produto, id=id, disponivel=True)
    return render(
        request, 'vendas/produto/exibe.html', {'produto': produto})


def get_menu_categorias():
    menu = Menu.objects.all()
    return menu


def get_carousel():
    carousel = Carousel.objects.all()
    return carousel


def get_descricao():
    descricao = Descricao.objects.all()
    return descricao


def get_tabela():
    tabela = Tabela.objects.all()
    return tabela

def get_rodape():
    rodape = Rodape.objects.all()
    return rodape