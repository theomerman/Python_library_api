from flask import Blueprint, request, jsonify

import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

from app.models import book
from app.db.database import db

add_book_route = Blueprint("add_book", __name__)
@add_book_route.route("/books", methods=["POST"])
def add_book():
    try:
        data = request.get_json()
        new_book = book.Book(title = data['title'], author = data['author'], year = data['year'], genre = data['genre'], price = data['price'], quantity = data['quantity'])
        db.session.add(new_book)
        db.session.commit()
        logging.info(f"Book added: {new_book}")
        return jsonify(data), 201
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An error occurred"}), 400

hello_route = Blueprint("hello", __name__)
@hello_route.route("/", methods=["GET"])
def hello():
    return "Hello, World!", 200

