from domain.leitor import leitor
from domain.livro import livro
from repositories.memory import DB

def criar_leitor(data):
    leitor = leitor(id = data.id, nome = data.nome, email = data.email)
    DB.leitores[data.id] = leitor
    return leitor

def listar_leitores():
    return list(DB.leitores.values())

def criar_livro(data):
    livro = livro(
        id = data.codigo,
        titulo = data.titulo,
        preco = data.preco,
        tipo = data.tipo,
        desconto_percentual = data.desconto_percentual

    )
    DB.livros[data.codigo] = livro
    return livro

def listar_livros():
    return list(DB.livros.values())

def buscar_livro(codigo: int):
    return DB.livros.get(codigo)

def alterar_preco_livro(codigo: int,  novo_preco: float):

    livro = DB.livros.get(codigo)
    if not livro:
        return None
    
    if novo_preco < 0:
        raise ValueError("O preço não pode ser menor que zero.")
    livro.preco = novo_preco
    return livro