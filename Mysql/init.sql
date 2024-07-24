CREATE DATABASE IF NOT EXISTS aura_essence;
USE aura_essence;

CREATE TABLE IF NOT EXISTS candle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(80) NOT NULL,
    description VARCHAR(200) NULL,
    price FLOAT NOT NULL,
    quantity INT NOT NULL
);

INSERT INTO candle (name, description, price, quantity) VALUES
('Lavender Bliss', 'A soothing lavender scent.', 19.99, 10),
('Vanilla Dream', 'A warm vanilla fragrance.', 14.99, 20),
('Citrus Burst', 'A refreshing citrus aroma.', 16.99, 15);
