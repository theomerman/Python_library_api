
from flask import Blueprint, request, jsonify

import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

from app.models import book
from app.db.database import db


get_books_route = Blueprint("get_books_route", __name__)

@get_books_route.route("/books", methods=["GET"])
def get_books():
    try:
        books = book.Book.query.all()
        tmp = []
        for i in books:
            tmp.append(
            {
                "isbn": i.isbn,
                "title": i.title,
                "author": i.author,
                "year": i.year,
                "genre": i.genre,
                "price": i.price,
                "quantity": i.quantity
            }
            )
        return tmp
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An error occurred"}), 400
