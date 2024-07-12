from app.models.book import Book

def test_modify_book(client, app):
    response = client.post('/books', json={
        'title': 'New Test Book',
        'author': 'New Test Author',
        'year': 2022,
        'genre': "New Test Genre",
        'price': 29.99,
        'quantity': 5
    })
    assert response.status_code == 201
    response = client.put('/books/1', json={
        'title': 'Updated Test Book',
        'author': 'Updated Test Author',
        'year': 2023,
        'genre': "Updated Test Genre", 
        'price': 39.99,
        'quantity': 10
    })
    assert response.status_code == 200
    assert response.get_json() == {"message": "Book updated"}
    # Verify the book was modified
    with app.app_context():
        assert Book.query.count() == 1
        assert Book.query.first().isbn == 1
        assert Book.query.first().title == "Updated Test Book"
        assert Book.query.first().author == "Updated Test Author"
        assert Book.query.first().year == 2023
        assert Book.query.first().genre == "Updated Test Genre"
        assert Book.query.first().price == 39.99
        assert Book.query.first().quantity == 10
