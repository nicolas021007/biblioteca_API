
class Livro:
    def __init__(self, codigo: int, titulo: str, preco: float, tipo: int, desconto_percentual: float = 0):
        if preco < 0:
            raise ValueError("O preço não pode ser negtivo.")
        if desconto_percentual < 0 or desconto_percentual > 100:
            raise ValueError("O desconto percentual deve estar entre 0  e 100.")
        if tipo not in [1,2]:
            raise ValueError("Tipo inválido. Use 1 para gratuito e 2 para pago.")
        
        self.codigo  = codigo
        self.titulo = titulo
        self.preco = preco
        self.tipo = tipo
        self.desconto_percentual = desconto_percentual

    def  preco_final(self) ->float:
        if self.tipo == 1:
            return 0.0
        desconto = self.preco *(self.desconto_percentual /100)
        return round(self.preco - desconto, 2)