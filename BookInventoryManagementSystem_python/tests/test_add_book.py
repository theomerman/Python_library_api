from app.models.book import Book

def test_add_book(client, app):
    response = client.post('/books', json={
        'title': 'New Test Book',
        'author': 'New Test Author',
        'year': 2022,
        'genre': 'New Test Genre',
        'price': 29.99,
        'quantity': 5
    })
    assert response.status_code == 201
    # assert response.get_json() == {"message": "Book added successfully!"}

    # Verify the book was added
    with app.app_context():
        assert Book.query.count() == 1
        assert Book.query.first().isbn == 1
        assert Book.query.first().title == "New Test Book"
        assert Book.query.first().author == "New Test Author"
        assert Book.query.first().year == 2022
        assert Book.query.first().genre == "New Test Genre"
        assert Book.query.first().price == 29.99
        assert Book.query.first().quantity == 5


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello, World!"


