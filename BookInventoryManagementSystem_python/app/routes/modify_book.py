
from flask import Blueprint, request, jsonify
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

from app.models import book
from app.db.database import db

modify_book_route = Blueprint("modify_book", __name__)

@modify_book_route.route("/books/<int:isbn>", methods=["PUT"])
def update_book(isbn):
    data = request.get_json()
    books = book.Book.query.get(isbn)
    if books is None:
        logging.error("Book not found")
        return jsonify({"error": "Book not found"}), 404
    if 'title' in data:
        books.title = data['title']
    if 'author' in data:
        books.author = data['author']
    if 'year' in data:
        books.year = data['year']
    if 'genre' in data:
        books.genre = data['genre']
    if 'price' in data:
        books.price = data['price']
    if 'quantity' in data:
        books.quantity = data['quantity']
    db.session.commit()
    logging.info(f"Book updated: {books}")
    return jsonify({"message": "Book updated"}), 200
