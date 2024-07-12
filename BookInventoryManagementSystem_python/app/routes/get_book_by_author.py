
from flask import Blueprint, request, jsonify
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

from app.models import book
from app.db.database import db

get_book_by_author_route = Blueprint("get_book_by_author_route", __name__)


@get_book_by_author_route.route("/books/author/<string:author>", methods=["GET"])
def get_books_by_author(author):
    books = book.Book.query.filter_by(author=author).all()
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
