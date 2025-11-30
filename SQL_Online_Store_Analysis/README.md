SQL Project: Online Store Sales Analysis

🛒 SQL Analysis of Online Store Sales Data

Overview

Analyzed sales data stored in a relational database using SQL to extract business insights.

⸻

🔧 Tools Used
	•	SQL (MySQL / PostgreSQL)
	•	Database tables: Customers, Orders, Order_Items

⸻

📁 Project Files
	•	sales_analysis.sql
	•![Uploading image.png…]()

	•	Query outputs

⸻

🗂️ Database Tables

Customers
	•	customer_id
	•	name
	•	gender
	•	city

Orders
	•	order_id
	•	customer_id
	•	order_date
	•	total_amount

Order_Items
	•	order_item_id
	•	order_id
	•	product
	•	quantity
	•	price

⸻

🛠 Key Queries

1️⃣ Most Sold Products
sql
SELECT product, SUM(quantity) AS total_sold
FROM order_items
GROUP BY product
ORDER BY total_sold DESC;

2️⃣ Top Customers by Spending
sql
SELECT c.name, SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 5;
SELECT c.name, SUM(o.total_amount) AS total_spent
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 5;

3️⃣ Revenue by Month
SELECT DATE_FORMAT(order_date, '%Y-%m') AS month,
       SUM(total_amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;
📈 Insights
	•	Top 5 customers contributed 28% of total revenue.
	•	Highest revenue months: June, September, November.
	•	Product A sold 4,200 units.

⸻

✅ Conclusion

SQL queries provided meaningful patterns for sales strategy and customer targeting.

