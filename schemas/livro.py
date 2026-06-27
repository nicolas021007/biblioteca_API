from pydantic import BaseModel
from domain.livro import TipoLivro


class LivroCreate(BaseModel):
    """
    Dados que o usuário precisa enviar para Criar um livro.
    """
    titulo:str
    preco:float
    tipo:TipoLivro
    desconto_percentual: float = 0


class LivroOut(BaseModel):
    """
    Dados que a API retorna.
    """
    codigo: str
    titulo:str
    preco:float
    tipo:TipoLivro
    desconto_percentual: float = 0

class LivroComPrecoFinal(BaseModel):

    """
    Retorna os dados da API, junto com o preço final
    
    """

    codigo: str
    titulo: str
    preco: float
    tipo: TipoLivro
    desconto_percentual: float = 0
    preco_final : float