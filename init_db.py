from database import engine, Base
from models import Books, Authors, BookAuthor, BooksCategory, Reviews
Base.metadata.create_all(bind=engine)
