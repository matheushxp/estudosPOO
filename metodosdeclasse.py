class Loja:
    
    taxa = 1.15

    def __init__(self, valor:float):
        self.valor_produto_bruto = valor

    def consultar_valor(self):
        valor_produto = self.valor_produto_bruto * self.taxa
        print(f'valor do produto: {valor_produto}')

    @classmethod
    def editar_taxa(cls, valor:float):
        cls.taxa = valor


quiosque = Loja(30.5)
mercado = Loja(20.33)

quiosque.consultar_valor()
mercado.consultar_valor()

quiosque.editar_taxa(1.35)


quiosque.consultar_valor()
mercado.consultar_valor()
