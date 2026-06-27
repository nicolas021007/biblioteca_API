from enum import Enum


class TipoLivro(int, Enum): 
    """
    Indica se o livro é gratuito ou pago."""

    GRATUITO = 1
    PAGO = 2

class Livro:
    def __init__(self, codigo:str, titulo:str,preco:float,  tipo:TipoLivro, desconto_percentual: float = 0,):
        """
        Validar antes de atribuir, para não existir objeto com dados inválidos."""

     

        if preco < 0:
            raise ValueError("O preço do livro não pode ser negativo.")
        if desconto_percentual < 0 or desconto_percentual > 100:
            raise ValueError("O desconto percentual deve estar entre 0 e 100.")
        
        if TipoLivro(tipo) == TipoLivro.GRATUITO and preco != 0:
            raise ValueError("Livro gratuito deve ter preço igual a 0.")

        self.codigo = codigo
        self.titulo = titulo
        self.preco = preco
        self.tipo = TipoLivro(tipo)
        self.desconto_percentual = desconto_percentual
        
    def preco_final(self) -> float:
        """
        Calcula o preço final do livro.
        Livros gratuitos sempre custam 0.0, independente do preço /desconto cadastrado.
        """

        if self.tipo == TipoLivro.GRATUITO:
            return 0.0
        
        desconto = self.preco *(self.desconto_percentual /100)

        return round(self.preco - desconto, 2)
    