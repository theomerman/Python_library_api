
from flask import Blueprint, request, jsonify
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)

from app.models import book
from app.db.database import db


get_book_by_genre_route = Blueprint("get_book_by_genre_route", __name__)

@get_book_by_genre_route.route("/books/genre/<int:genre>", methods=["GET"])
def get_books_by_genre(genre):
    books = book.Book.query.filter_by(genre=genre).all()
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
