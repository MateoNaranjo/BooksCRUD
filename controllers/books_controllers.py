import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from flask import Blueprint, jsonify, request
from services.book_services import get_all_books, get_book_by_id, create_book, update_book

books_bp = Blueprint('books_bp', __name__)

@books_bp.route('/books', methods=['GET'])
def list_books():
    return jsonify(get_all_books())

@books_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    return jsonify(get_book_by_id(book_id))

@books_bp.route('/books', methods=['POST'])
def add_book():
    data = request.json
    return jsonify(create_book(data))

@books_bp.route('/books/<int:book_id>', methods=['PUT'])
def modify_book(book_id):
    data = request.json
    return jsonify(update_book(book_id, data))


