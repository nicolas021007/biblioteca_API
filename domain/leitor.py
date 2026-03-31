from dataclasses import dataclass

@dataclass(frozen = True)
class leitor:
    id: int
    nome: str
    email: str