from pydantic import BaseModel, EmailStr

class LeitorCreate(BaseModel):
    id: int
    nome:str
    email: EmailStr


class LeitorOut(BaseModel):
    id: int
    nome:str
    email: EmailStr 