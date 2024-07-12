from app.db.database import db

class Book(db.Model):
    isbn = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    author = db.Column(db.String(255), nullable = False)
    year = db.Column(db.Integer, nullable = False)
    genre = db.Column(db.String(255), nullable = False)
    price = db.Column(db.Float, nullable = False)
    quantity = db.Column(db.Integer, nullable = False)

    def __str__(self):
        return f"{self.title} by {self.author}"
    def __repr__(self):
        return f"{self.title} by {self.author} ISBN: {self.isbn} Quantity: {self.quantity}"
    
