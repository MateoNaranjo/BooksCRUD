import mysql.connector

def connect_root():
        try:
            conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="hondazfe16c"
            )
            
            return conn
            
        except Exception as e:
            return f'Error conexion a mysql {e}'
        
def connect_db():
        try:
            conn=mysql.connector.connect(
                host="localhost",
                user="root",
                password="hondazfe16c",
                database="books_crud"
            )
            
            return conn
            
        except Exception as e:
            return f'Error conexion a la base de datos {e}'
    

root=connect_root()
base=connect_db()

print(root)
print(base)