from flask import Blueprint, jsonify, request

books_bp = Blueprint('books_bp', __name__)

@books_bp.route('/books', methods=['GET'])

@books_bp.route('/books/<int:book_id>', methods=['GET'])

@books_bp.route('/books', methods=['POST'])

@books_bp.route('/books/<int:book_id>', methods=['PUT'])

@books_bp.route('/books/<int:book_id>', methods=['DELETE'])

