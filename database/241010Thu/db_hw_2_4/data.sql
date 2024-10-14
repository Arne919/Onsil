-- Active: 1728633289184@@127.0.0.1@3306
DROP TABLE orders;

-- orders 테이블 생성: 주문 정보를 저장하기 위한 테이블
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,   -- 주문 ID (기본 키)
    customer_id INTEGER,
    order_date DATE,                -- 주문 날짜 (날짜 타입)
    price INTEGER,
    FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

ALTER TABLE orders ADD COLUMN price INTEGER;

ALTER TABLE orders DROP COLUMN total_amount;

-- orders 테이블에 데이터 삽입
INSERT INTO orders (order_id, customer_id, order_date, price) VALUES
    (1, 1, '2023-07-15', 50),      -- 2023년 7월 15일 주문, 총 주문 금액: 50.99
    (2, 2, '2023-07-16', 75),      -- 2023년 7월 16일 주문, 총 주문 금액: 75.50
    (3, 3, '2023-07-17', 30);      -- 2023년 7월 17일 주문, 총 주문 금액: 30.25

SELECT orders.order_id, customers.name, orders.order_date, orders.price
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id;