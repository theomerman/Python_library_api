
from flask import Blueprint, request, jsonify
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

from app.models import book
from app.db.database import db


get_book_by_id_route = Blueprint("get_book_by_id_route", __name__)

@get_book_by_id_route.route("/books/<int:isbn>", methods=["GET"])
def get_book(isbn):
    books = book.Book.query.get(isbn)
    if books is None:
        logging.error("Book not found")
        return jsonify({"error": "Book not found"}), 404
    books = { "isbn": books.isbn, "title": books.title, "author": books.author, "year": books.year, "genre": books.genre, "price": books.price, "quantity": books.quantity }
    return jsonify(books)
