CREATE DATABASE IF NOT EXISTS book_system;

USE book_system;

CREATE TABLE IF NOT EXISTS book (
    isbn INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    genre VARCHAR(255) NOT NULL,
    price DOUBLE NOT NULL,
    quantity INT NOT NULL
);

CREATE TABLE IF NOT EXISTS sell(
    id INT PRIMARY KEY AUTO_INCREMENT,
    quantity INT NOT NULL
);

CREATE TABLE IF NOT EXISTS detail_sell(
    id INT PRIMARY KEY AUTO_INCREMENT,
    venta_id INT NOT NULL,
    book_isbn INT NOT NULL,
    FOREIGN KEY (venta_id) REFERENCES sell(id),
    FOREIGN KEY (book_isbn) REFERENCES book(isbn)
);


