from fastapi import APIRouter, HTTPException
from  pydantic import BaseModel
from schemas.livro import LivroCreate, LivroOut, LivroComPrecoFinal
from services.biblioteca_service import (
    alterar_preco_livro,
    buscar_livro,
    criar_livro,
    listar_livros,
)

router = APIRouter(prefix= "/livros", tags=["Livros"])

class AlterarPrecoInput(BaseModel):
    preco: float

@router.post("", response_model=LivroOut)
def post_livro(data: LivroCreate):
    try:
        return criar_livro(data)
    except ValueError as erro:
        raise HTTPException(status_code=400 , detail = str(erro))

@router.get("", response_model=list[LivroOut])
def get_livros():
    return listar_livros()

@router.get("/{codigo}", response_model= LivroOut)
def get_livro(codigo: str):
    livro = buscar_livro(codigo)

    if not livro:
        raise HTTPException(status_code=404,detail ="Livro não encontrado!")
        
    return livro
@router.put("/{codigo}/preco", response_model =LivroOut)

def put_preco_livro(codigo: str, data: AlterarPrecoInput):
    
    try:
        livro = alterar_preco_livro(codigo,data.preco)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail = str(erro))
    
    if not livro:
        raise HTTPException(status_code=400, detail ="Livro não encontrado!")
    
    return livro
    
@router.get("/{codigo}/preco_final", response_model = LivroComPrecoFinal)

def get_preco_final(codigo: str):

    livro = buscar_livro(codigo)

    if not livro:
        raise HTTPException(status_code= 404, detail="Livro não encontrado!")
    
    return LivroComPrecoFinal(
        codigo = livro.codigo, 
        titulo=livro.titulo,
        preco=livro.preco,
        tipo=livro.tipo,
        desconto_percentual=livro.desconto_percentual,
        preco_final=livro.preco_final(),

    )