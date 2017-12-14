from django import forms

OPCOES_DE_QUANTIDADE_PARA_O_PRODUTO = [(i, str(i)) for i in range(1, 21)]

class FormularioParaAdicaoDeProdutosAoCarrinho(forms.Form):
    quantidade = forms.TypedChoiceField(label="Quantidade ",
                                        choices=OPCOES_DE_QUANTIDADE_PARA_O_PRODUTO,
                                        coerce=int,
                                        widget=forms.Select(attrs={'class': 'form-control input-sm',
                                                                   'style': 'margin-left: 6px; margin-right: 6px; max-width: 60px; text-center'}))

    atualizar = forms.BooleanField(required=False,             # O default é required=True
                                   initial=False,
                                   widget=forms.HiddenInput)