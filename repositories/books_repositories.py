import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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

def insert_books(book):
    try:
        conn=connect_db()
        if conn is None:
            return 'Error: conexión fallida'
        cur=conn.cursor()
        sql="INSERT INTO books (title, author, year) VALUES (%s, %s, %s)"
        values=(book['title'], book['author'], book['timestamp'].year)
        cur.execute(sql, values)
        conn.commit()
        conn.close()
        return 'Book inserted'
    except Exception as e:
        return f'Error insertando libro {e}'
    
def view_books():
    try:
        conn=connect_db()
        if conn is None:
            return 'Error: conexión fallida'
        cur=conn.cursor()
        cur.execute("SELECT * FROM books")
        books=cur.fetchall()
        conn.close()
        return books
    except Exception as e:
        return f'Error mostrando libros {e}'
    
    
print(insert_books(books_list[0]))
print(view_books())

