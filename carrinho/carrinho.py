from decimal import Decimal
from django.conf import settings
from vendas.models import Produto


class Carrinho(object):

    def __init__(self, request):
        self.session = request.session
        self.carrinho = self.session.get(settings.CARRINHO_SESSION_ID)
        if not self.carrinho:
            self.carrinho = self.session[settings.CARRINHO_SESSION_ID] = {}

    def __len__(self):
        return sum(item['quantidade'] for item in self.carrinho.values())

    def get_lista_de_itens_de_carrinho(self):
        lista = []
        for item in self.carrinho.values():
            produto = Produto.objects.get(id=item['id'])
            lista.append({'id': item['id'],
                          'quantidade': item['quantidade'],
                          'preco': Decimal(item['preco']),
                          'preco_total': item['quantidade'] * Decimal(item['preco']),
                          'produto': produto})
        return lista

    def adicionar(self, produto, quantidade=1, atualiza_quantidade=False):
        produto_id = str(produto.id)

        if produto_id not in self.carrinho:
            self.carrinho[produto_id] = {'id': produto_id, 'quantidade': 0, 'preco': str(produto_id.preco)}

        if atualiza_quantidade:
            self.carrinho[produto_id]['quantidade'] = quantidade
        else:
            self.carrinho[produto_id]['quantidade'] += quantidade
        self.salvar()

    def remover(self, produto):
        """ Remove a produto from the carrinho. """

        produto_id = str(produto.id)

        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.salvar()  # O método salvar é chamado para que o carrinho seja salvo na sessão

    def salvar(self):
        self.session[settings.CARRINHO_SESSION_ID] = self.carrinho
        self.session.modified = True

    def limpar(self):
        self.session[settings.CARRINHO_SESSION_ID] = {}
        self.session.modified = True

    def get_preco_total(self):
        return sum(Decimal(item['preco']) * item['quantidade'] for item in self.carrinho.values())
