from __future__ import annotations
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from core.db import Base


class Genre(Base):
    __tablename__ = "Genre"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    genre_name = Column(String(15), nullable=False, unique=True)


genres = Genre.__table__


AuthorBook = Table('AuthorBook',
                   Base.metadata,
                   Column('id', Integer, primary_key=True),
                   Column('author_id', Integer, ForeignKey('authors.id')),
                   Column('book_id', Integer, ForeignKey('books.id')),
                   )


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name_book = Column(String(15), nullable=False, unique=True)
    number_of_pages = Column(Integer)
    genre_id = Column(Integer, ForeignKey('Genre.id'))
    publication = Column(Boolean, default=False, nullable=False)
    author = relationship('Author', secondary=AuthorBook, backref='books')


books = Book.__table__


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(15), nullable=False, unique=True)
    date_of_birth = Column(DateTime(timezone=True))
    book = relationship('Book', secondary=AuthorBook, backref='authors')


authors = Author.__table__
