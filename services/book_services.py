from models.books_models import Books
from repositories.books_repositories import insert_book, view_books, view_book_by_id, update_book

def get_all_books():
    return view_books()

def get_book_by_id(book_id):
    return view_book_by_id(book_id)

def create_book(data):
    book = Books(id=None, title=data['title'], author=data['author'], timestamp=datetime.now())
    return insert_book(book)

def update_book(book_id, data):
    book = Books(id=book_id, title=data['title'], author=data['author'], timestamp=datetime(data['year'], 1, 1))
    return update_book(book)
