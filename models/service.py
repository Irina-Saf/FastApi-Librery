# обмен с бд
from sqlalchemy.orm import Session
from models.models import Genre, Book, Author, AuthorBook
from .schemas import (GenreCreate, BookCreate,
                      AuthorCreate, GenreUpdate, BookUpdate)


def get_genre_list(db: Session):
    return db.query(Genre).all()


def get_genre_id(db: Session, id: int):
    return db.query(Genre).filter(Genre.id == id).first()


def create_genre(db: Session, item: GenreCreate):
    genre = Genre(**item.model_dump())
    db.add(genre)
    db.commit()
    db.refresh(genre)
    return genre


def delete_genre(db: Session, id: int):
    genre = db.query(Genre).filter(Genre.id == id).delete()
    db.commit()
    return genre


def update_genre(db: Session, id: int, item: GenreUpdate):
    genre = db.query(Genre).filter(Genre.id == id).first()
    genre.genre_name = item.genre_name
    db.add(genre)
    db.commit()
    db.refresh(genre)
    return genre


def get_book_list(db: Session):
    return db.query(Book).all()


def get_book_id(db: Session, id: int):
    return db.query(Book).filter(Book.id == id).first()


def create_book(db: Session, item: BookCreate):
    book = Book()

    book.name_book = item.name_book
    book.number_of_pages = item.number_of_pages
    book.genre_id = item.genre_id
    book.publication = item.publication

    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, id: int):
    book = db.query(Book).filter(Book.id == id).delete()
    db.commit()
    return book


def update_book(db: Session, id: int, item: BookUpdate):
    book = db.query(Book).filter(Book.id == id).first()
    for var, value in vars(item).items():
        setattr(book, var, value) if value else None
    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def get_author_list(db: Session):
    return db.query(Author).all()


def get_author_id(db: Session, id: int):
    return db.query(Author).filter(Author.id == id).first()


def create_author(db: Session, item: AuthorCreate):
    author = Author(**item.model_dump())
    db.add(author)
    db.commit()
    db.refresh(author)
    return author


def delete_author(db: Session, id: int):
    author = db.query(Author).filter(Author.id == id).delete()
    db.commit()
    return author


def update_author(db: Session, id: int, item: BookUpdate):
    author = db.query(Author).filter(Author.id == id).first()
    for var, value in vars(item).items():
        setattr(author, var, value) if value else None

    db.add(author)
    db.commit()
    db.refresh(author)
    return author
