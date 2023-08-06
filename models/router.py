from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.utils import get_db
from . import service
from . schemas import (AuthorCreate, AuthorList, AuthorUpdate, GenreCreate,
                       GenreList, BookList, BookCreate, GenreUpdate,
                       BookUpdate)


router_genre = APIRouter(
    prefix="/genre",
    tags=["genre"]
)


@router_genre.get("/", response_model=List[GenreList])
def genre_list(db: Session = Depends(get_db)):
    genres = service.get_genre_list(db)
    return genres


@router_genre.get("/{id}")
def genre_list_2(db: Session = Depends(get_db), id: int = None):
    genres_id = service.get_genre_id(db, id)
    return genres_id


@router_genre.post("/")
def genre_list_3(item: GenreCreate, db: Session = Depends(get_db)):
    genre = service.create_genre(db, item)
    return genre


@router_genre.delete("/")
def del_genre(db: Session = Depends(get_db), id: int = None):
    deleted = service.delete_genre(db, id)
    return {"genre_deleted": deleted}


@router_genre.patch("/")
def patch_genre(db: Session = Depends(get_db),
                id: int = None,
                item: GenreUpdate = None):
    patch_genre = service.update_genre(db, id, item)
    return patch_genre


router_book = APIRouter(
    prefix="/book",
    tags=["book"]
)


@router_book.get("/", response_model=List[BookList])
def book_list(db: Session = Depends(get_db)):
    book = service.get_book_list(db)
    return book


@router_book.get("/{id}")
def book_list_2(db: Session = Depends(get_db), id: int = None):
    book_id = service.get_book_id(db, id)
    return book_id


@router_book.post("/")
def book_list_3(item: BookCreate, db: Session = Depends(get_db)):
    book = service.create_book(db, item)
    return book


@router_book.delete("/")
def del_book(db: Session = Depends(get_db), id: int = None):
    deleted = service.delete_book(db, id)
    return {"book_deleted": deleted}


@router_book.patch("/")
def patch_book(db: Session = Depends(get_db),
               id: int = None,
               item: BookUpdate = None):
    patch_book = service.update_book(db, id, item)
    return patch_book


router_author = APIRouter(
    prefix="/author",
    tags=["author"]
)


@router_author.get("/", response_model=List[AuthorList])
def author_list(db: Session = Depends(get_db)):
    author = service.get_author_list(db)
    return author


@router_author.get("/{id}")
def author_list_2(db: Session = Depends(get_db), id: int = None):
    author_id = service.get_author_id(db, id)
    return author_id


@router_author.post("/")
def author_list_3(item: AuthorCreate, db: Session = Depends(get_db)):
    author = service.create_author(db, item)
    return author


@router_author.delete("/")
def del_author(db: Session = Depends(get_db), id: int = None):
    deleted = service.delete_author(db, id)
    return {"author_deleted": deleted}


@router_author.patch("/")
def patch_author(db: Session = Depends(get_db),
                 id: int = None,
                 item: AuthorUpdate = None):
    patch_author = service.update_author(db, id, item)
    return patch_author
