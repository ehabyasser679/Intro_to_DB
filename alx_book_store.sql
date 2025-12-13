CREATE DATABASE IF NOT EXISTS alx_book_store;

CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    author_name VARCHAR(215)
);

CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(130),
    author_id INT REFERENCES Authors(author_id),
    price DOUBLE PRECISION,
    publication_date DATE
);

CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(215),
    email VARCHAR(215),
    address TEXT
);

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    order_date DATE
);

CREATE TABLE Order_Details (
    order_detail_id INT PRIMARY KEY,
    order_id INT REFERENCES Orders(order_id),
    book_id INT REFERENCES Books(book_id),
    quantity DOUBLE PRECISION
);
