
from flask import Blueprint, request, jsonify
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

from app.models import book
from app.db.database import db

delete_book_route = Blueprint("delete_book_route", __name__)

@delete_book_route.route("/books/<int:isbn>", methods=["DELETE"])
def delete_book(isbn):
    books = book.Book.query.get(isbn)
    if books is None:
        logging.error("Book not found")
        return jsonify({"error": "Book not found"}), 404
    db.session.delete(books)
    db.session.commit()
    logging.info(f"Book deleted: {books}")
    return jsonify({"message": "Book deleted"}), 200

