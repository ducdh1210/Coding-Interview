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

-- Query 4: Product sales quantity by quarter
SELECT product_id, product_name,
       CASE 
           WHEN strftime('%m', sale_date) IN ('01','02','03') THEN 'Q1'
           WHEN strftime('%m', sale_date) IN ('04','05','06') THEN 'Q2'
           WHEN strftime('%m', sale_date) IN ('07','08','09') THEN 'Q3'
           ELSE 'Q4'
       END as quarter,
       SUM(quantity) as quarterly_quantity
FROM sales
GROUP BY product_id, product_name, quarter;