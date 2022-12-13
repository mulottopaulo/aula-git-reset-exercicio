class Promocao:
    
    @staticmethod
    def aplica_desconto(produto, pct_desconto):
        desconto = Promocao.calcula_desconto(produto)
        valor_final = produto.valor_venda - desconto
        return valor_final

    @classmethod
    def calcula_desconto(cls, produto, pct_desconto):
        desconto_total = produto.valor_venda * (pct_desconto/100)
        return desconto_total