from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .carrinho import Carrinho
from vendas.models import Produto
from .forms import FormularioParaAdicaoDeProdutosAoCarrinho

@require_POST            # Para permitir que esta view só possa ser executada via POST pois ela modifica dados
def adicionar_ao_carrinho(request, id_produto):   # Essa view recebe o id do produto
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id_produto)
    # a view valida o formulário
    form = FormularioParaAdicaoDeProdutosAoCarrinho(request.POST)
    if form.is_valid():  # executa as rotinas de validação para todos os campos do formulário. Quando este método
                         # é chamado, se todos os campos tiverem dados válidos ele irá:
                         # - retornar True
                         # - colocar os dados do form no atributo cleaned_data do formulário
        cd = form.cleaned_data

        # Se o formulário for válido, adicionamos ou atualizamos o
        # produto no carrinho na qtd informada.
        carrinho.adicionar(produto=produto,
                 quantidade=cd['quantidade'],
                 atualiza_quantidade=cd['atualizar'])
    # A view redireciona para o detalhes_do_carrinho URL que irá exibir o conteúdo do carrinho.
    return redirect('carrinho:detalhes_do_carrinho') # Este redirect fará com que a requisição seja redirecionada
                                                     # para http://127.0.0.1:8000/carrinho


def detalhes_do_carrinho(request):
    carrinho = Carrinho(request)

    lista = carrinho.get_lista_de_itens_de_carrinho()

    for item in lista:
        item['atualizar_quantidade_form'] = FormularioParaAdicaoDeProdutosAoCarrinho(
            initial={'quantidade': item['quantidade'], 'atualizar': True})

    return render(request, 'carrinho/exibe.html', {'carrinho': carrinho, 'lista': lista})

def remover_do_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id_produto)
    carrinho.remover(produto)
    return redirect('carrinho:detalhes_do_carrinho')
