from app.models.book import Book

def test_delete_book(client, app):
    response = client.post('/books', json={
        'title': 'New Test Book',
        'author': 'New Test Author',
        'year': 2022,
        'genre': 'New Test Genre',
        'price': 29.99,
        'quantity': 5
    })
    response = client.delete('/books/1')
    assert response.status_code == 200
    assert response.get_json() == {"message": "Book deleted"}
    # Verify the book was deleted
    with app.app_context():
        assert Book.query.count() == 0
