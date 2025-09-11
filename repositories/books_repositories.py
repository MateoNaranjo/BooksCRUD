import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.books_models import Books
from config.conexion import connect_db 
from datetime import datetime

books_list=[
    {
        'title':'El principito',
        'author':'Antoine de Saint-Exupéry',
        'timestamp':datetime.now()
    },
    {
        'title':'Cien años de soledad',
        'author':'Gabriel García Márquez',
        'timestamp':datetime.now()
    },
    {
        'title':'Don Quijote de la Mancha',
        'author':'Miguel de Cervantes',
        'timestamp':datetime.now()
    }
    
]

def insert_book(book: Books):
    try:
        conn = connect_db()
        cur = conn.cursor()
        sql = "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)"
        values = (book.title, book.author, book.timestamp.year)
        cur.execute(sql, values)
        conn.commit()
        conn.close()
        return 'Libro insertado correctamente'
    except Exception as e:
        return f'Error insertando libro: {e}'

    
def view_books():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT id, title, author, year FROM books")
        rows = cur.fetchall()
        conn.close()
        books = [Books(id=row[0], title=row[1], author=row[2], timestamp=datetime(row[3], 1, 1)) for row in rows]
        return [book.serialize() for book in books]
    except Exception as e:
        return f'Error mostrando libros: {e}'

    
def update_book(book: Books):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute(
            "UPDATE books SET title=%s, author=%s, year=%s WHERE id=%s",
            (book.title, book.author, book.timestamp.year, book.id)
        )
        conn.commit()
        conn.close()
        return 'Libro actualizado correctamente'
    except Exception as e:
        return f'Error actualizando libro: {e}'


def delete_book(book_id):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE id=%s", (book_id,))
        conn.commit()
        conn.close()
        return 'Libro eliminado correctamente'
    except Exception as e:
        return f'Error eliminando libro: {e}'
    
def view_book_by_id(book_id):
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("SELECT id, title, author, year FROM books WHERE id=%s", (book_id,))
        row = cur.fetchone()
        conn.close()
        if row:
            book = Books(id=row[0], title=row[1], author=row[2], timestamp=datetime(row[3], 1, 1))
            return book.serialize()
        else:
            return None
    except Exception as e:
        return f'Error mostrando libro: {e}'



print(view_book_by_id(11))  
    


