-- Active: 1728632590229@@127.0.0.1@3306
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    order_date DATE,
    total_amount REAL
);

INSERT INTO orders (order_id, order_date, total_amount) VALUES
    (1, '2023-07-15', 50.99),
    (2, '2023-07-16', 75.50),
    (3, '2023-07-17', 30.25);

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    phone TEXT
);

INSERT INTO customers (name, email, phone) VALUES
    ('허균', 'hong.gildong@example.com', '010-1234-5678'),
    ('김영희', 'kim.younghee@example.com', '010-9876-5432'),
    ('이철수', 'lee.cheolsu@example.com', '010-5555-4444');

DELETE 
FROM orders 
WHERE order_id = 3;

UPDATE customers 
SET name = '홍길동' 
WHERE customer_id = 1;

SELECT * 
FROM orders;

SELECT * 
FROM customers;

