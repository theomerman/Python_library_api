
from flask import Blueprint
from flask import Flask
from app.routes.add_book import add_book_route
from app.routes.delete_book import delete_book_route
from app.routes.get_book_by_author import get_book_by_author_route
from app.routes.get_book_by_genre import get_book_by_genre_route
from app.routes.get_book_by_id import get_book_by_id_route
from app.routes.get_book_by_title import get_book_by_title_route
from app.routes.add_book import hello_route
from app.routes.modify_book import modify_book_route


def register_blueprints(app):
    app.register_blueprint(add_book_route)
    app.register_blueprint(delete_book_route)
    app.register_blueprint(get_book_by_author_route)
    app.register_blueprint(get_book_by_genre_route)
    app.register_blueprint(get_book_by_id_route)
    app.register_blueprint(get_book_by_title_route)
    app.register_blueprint(modify_book_route)
    app.register_blueprint(hello_route)

