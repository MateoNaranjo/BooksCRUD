from conexion import connect_root, connect_db




def create_database():
        try:
            connRT=connect_root()
            if connRT is None:
                return 'Error: conexión fallida'
            cur=connRT.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS books_crud")
            connRT.close()
            return 'Database created'
        except Exception as e:
            return f'Error creando base {e}'
        
def create_table():
        try:
            connDB=connect_db()
            if connDB is None:
                return 'Error: conexión fallida'
            cur=connDB.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS books (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), year INT)")
            connDB.close()
            return 'Table created'
        except Exception as e:
            return f"error creando tabla {e}"
        
