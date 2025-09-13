📚 BooksCRUDAPI
Este proyecto es una API RESTful desarrollada en Python usando Flask, diseñada para gestionar libros. La arquitectura está basada en el patrón MVC, separando claramente los controladores, servicios y repositorios. Los datos se almacenan en una base de datos relacional, lo que permite persistencia entre ejecuciones.

🗂️ Estructura del Proyecto
main.py: Punto de entrada de la aplicación Flask. Registra los blueprints y lanza el servidor.

controllers/books_controllers.py: Define los endpoints HTTP relacionados con libros.

services/book_services.py: Contiene la lógica de negocio y validación.

repositories/books_repository.py: Interactúa directamente con la base de datos.

models/books.py: Define la clase Books que representa la estructura de los datos.

requirements.txt: Lista de dependencias necesarias para ejecutar el proyecto.

🔗 Endpoints disponibles
Método	Endpoint	Descripción
GET	/books	Obtiene la lista de todos los libros.
GET	/books/<id>	Obtiene la información de un libro por su ID.
POST	/books	Crea un nuevo libro. Requiere JSON con title, author, year.
PUT	/books/<id>	Actualiza los datos de un libro existente.
DELETE	/books/<id>	Elimina un libro por su ID.
🧪 Ejemplos de uso con curl
Obtener todos los libros:

bash
curl -i http://localhost:5000/books
Obtener un libro por ID:

bash
curl -i http://localhost:5000/books/11
Crear un nuevo libro:

bash
curl -i -X POST http://localhost:5000/books \
  -H "Content-Type: application/json" \
  -d '{"title": "Cien años de soledad", "author": "Gabriel García Márquez", "year": 1967}'
Actualizar un libro existente:

bash
curl -i -X PUT http://localhost:5000/books/11 \
  -H "Content-Type: application/json" \
  -d '{"title": "El amor en los tiempos del cólera", "author": "Gabriel García Márquez", "year": 1985}'
Eliminar un libro:

bash
curl -i -X DELETE http://localhost:5000/books/11
⚙️ Requisitos
Python 3.12+

Flask

psycopg2 / sqlite3 (según la base de datos que uses)

🚀 Instalación y ejecución
Instala las dependencias:


bash
pip install -r requirements.txt
Ejecuta la aplicación:

bash
python main.py
📝 Notas
Los datos se almacenan en una base de datos relacional, por lo que persisten entre ejecuciones.

Los endpoints devuelven respuestas en formato JSON y utilizan códigos de estado HTTP apropiados.

Puedes extender el proyecto para incluir validaciones, autenticación, paginación o documentación automática con Swagger.
