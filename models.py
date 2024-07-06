from database import Base
from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, Float, CheckConstraint
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

class BooksCategory(Base):
    __tablename__ = 'books_category'
    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String(32), unique=True, index=True)
    books = relationship('Books', back_populates='books_category')

    def __repr__(self):
        return f'< Category = {self.category_name}>'


class Authors(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), index=True)
    surname = Column(String(64), index=True)
    book_author = relationship('BookAuthor', back_populates='authors')

    def __repr__(self):
        return f"< First name = {self.name}  - Surname = {self.surname} >"


class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64), unique=True, index=True)
    category = Column(Integer, ForeignKey('books_category.id'))
    description = Column(Text, index=True)
    ISBN = Column(Text, unique=True, index=True)
    image_path = Column(String, index=True, nullable=True)
    year = Column(Integer, index=True)
    price = Column(Float, index=True)
    book_category = relationship('BooksCategory', back_populates='books')
    book_author = relationship('BookAuthor', back_populates='books')

    def __repr__(self):
        return f"<Title = {self.title} - category = {self.category}>"


class BookAuthor(Base):
    __tablename__ = 'books_authors'
    id = Column(Integer, primary_key=True, index=True)
    books_id = Column(Integer, ForeignKey('books.id'))
    authors_id = Column(Integer, ForeignKey('authors.id'))
    book = relationship('Books', back_populates='books_authors')
    author = relationship('Authors', back_populates='books_authors')
    review = relationship('Reviews', back_populates='books_authors')

    def __repr__(self):
        return f"<Book_title = {self.books_id} - book_author = {self.authors_id}>"


class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(Text, index=True)
    star_given = Column(Integer, CheckConstraint('star_given >= 1 AND star_given <= 5', name='check_star_given'))
    user = Column(String(64), index=True)
    book_id = Column(Integer, ForeignKey('books_authors.id'))
    book = relationship('BookAuthor', back_populates='reviews')

    def __repr__(self):
        return f"<Comment = {self.comment} - user = {self.user} - book = {self.book_id}>"