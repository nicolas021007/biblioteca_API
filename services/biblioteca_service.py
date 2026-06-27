from domain.leitor import Leitor
from domain.livro import Livro
from repositories.memory import db
from uuid import uuid4

def criar_leitor(data):
    novo_id = str(uuid4())
    leitor = Leitor(
        id = novo_id,
        nome = data.nome,
        email = data.email)
    db.leitores[novo_id] = leitor

    return leitor

def listar_leitores():
    return list(db.leitores.values())

def criar_livro(data):
    novo_codigo = str(uuid4())

    livro = Livro(
        codigo = novo_codigo,
        titulo = data.titulo,
        preco = data.preco,
        tipo = data.tipo,
        desconto_percentual = data.desconto_percentual

    )
    db.livros[novo_codigo] = livro
    return livro

def listar_livros():
    return list(db.livros.values())

def buscar_livro(codigo: int):
    return db.livros.get(codigo)

def alterar_preco_livro(codigo: int,  novo_preco: float):

    livro = db.livros.get(codigo)
    if not livro:
        return None
    
    if novo_preco < 0:
        raise ValueError("O preço não pode ser menor que zero.")
    livro.preco = novo_preco


    return livro