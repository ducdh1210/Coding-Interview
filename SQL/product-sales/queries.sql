-- Query 1: Total sales quantity by product
SELECT product_id, product_name, SUM(quantity) as total_quantity
FROM sales
GROUP BY product_id, product_name;

-- Query 2: Total revenue by product
SELECT product_id, product_name, SUM(quantity * price) as total_revenue
FROM sales
GROUP BY product_id, product_name;

-- Query 3: Monthly sales quantity
SELECT strftime('%Y-%m', sale_date) as month, SUM(quantity) as monthly_quantity
FROM sales
GROUP BY strftime('%Y-%m', sale_date);


