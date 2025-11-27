-- Top selling products
SELECT product, SUM(quantity) AS total_sold
FROM order_items
GROUP BY product
ORDER BY total_sold DESC
LIMIT 5;
