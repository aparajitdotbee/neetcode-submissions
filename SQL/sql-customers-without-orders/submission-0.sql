-- Write your query below

SELECT DISTINCT(name) FROM customers
LEFT JOIN orders ON customers.id = orders.customer_id
WHERE orders.id IS NULL;