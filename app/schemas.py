from typing import Optional

from pydantic import BaseModel


# Schema para o usuário de entrada (criação)
class UserCreate(BaseModel):
    id: Optional[int]
    username: str
    email: str
    full_name: Optional[str] = None


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None


# Schema para o usuário de saída
class User(BaseModel):
    id: int
    username: str
    email: str
    full_name: Optional[str] = None

    class Config:
        orm_mode = True
