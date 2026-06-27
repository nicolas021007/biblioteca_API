from pydantic import BaseModel, EmailStr

class LeitorCreate(BaseModel):
    """Dados que o usuário envia para criar o leitor."""
    nome:str
    email: EmailStr


class LeitorOut(BaseModel):
    """Dados que a API retorna, já com o ID atribuido."""
    id: str
    nome:str
    email: EmailStr 