

from flask import Flask, jsonify, request
from app.db.database import db
import logging

from app.routes import register_blueprints

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)
logging.info('Admin logged in')

def create_app(database_uri="mysql+mysqlconnector://root:password@localhost/book_system"):

    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    register_blueprints(app)

    return app
