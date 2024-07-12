from flask import Blueprint, request, jsonify
import logging

# from app.routes.get_book_by_author import get_books_by_author

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

from app.models import book
from app.db.database import db


get_book_by_title_route = Blueprint("get_book_by_title", __name__)

@get_book_by_title_route.route("/books/title/<string:title>", methods=["GET"])
def get_books_by_title(title):
    books = book.Book.query.filter_by(title=title).all()
    tmp = []
    for i in books:
        tmp.append({
            "isbn": i.isbn,
            "title": i.title,
            "author": i.author,
            "year": i.year,
            "genre": i.genre,
            "price": i.price,
            "quantity": i.quantity
        })
    return tmp


