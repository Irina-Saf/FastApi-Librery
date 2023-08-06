# from __future__ import annotations
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# from models import Genre


class GenreBase(BaseModel):
    genre_name: str

    class Config:
        orm_mode = True


# класс для вывода жанров (то, что мы забираем из bd)
class GenreList(GenreBase):
    id: int


class GenreCreate(GenreBase):
    pass


class GenreUpdate(GenreBase):
    pass


class AuthorBase(BaseModel):
    name: str
    date_of_birth: Optional[datetime]

    class Config:
        orm_mode = True


class AuthorList(AuthorBase):
    id: int


class AuthorCreate(AuthorBase):
    pass


class AuthorUpdate(AuthorBase):
    pass


class BookBase(BaseModel):
    name_book: str
    number_of_pages: int
    genre_id: int
    publication: bool = False

    class Config:
        orm_mode = True


class BookList(BookBase):
    id: int
    author: List[AuthorList]


class BookCreate(BookBase):
    author_id: List[int]
    pass


class BookUpdate(BookBase):
    pass
