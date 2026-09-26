CREATE DATABASE
superstore_analysis;
USE superstore_analysis;


CREATE TABLE superstore (
    row_id INT,
    order_id VARCHAR(50),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_id VARCHAR(50),
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    country VARCHAR(50),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    region VARCHAR(50),
    product_id VARCHAR(50),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(255),
    sales DECIMAL(12,4)
);
SELECT COUNT(*) AS total_rows
FROM superstore;
SELECT
    COUNT(*) AS total_rows,
    COUNT(DISTINCT order_id) AS unique_orders,
    COUNT(DISTINCT customer_id) AS unique_customers,
    COUNT(DISTINCT product_id) AS unique_products
FROM superstore;

SELECT
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore;

SELECT
    ROUND(AVG(sales), 2) AS average_sales
FROM superstore;

SELECT
    ROUND(MAX(sales), 2) AS maximum_sale
FROM superstore;

SELECT
    ROUND(MIN(sales), 2) AS minimum_sale
FROM superstore;

SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY category
ORDER BY total_sales DESC;

SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    ROUND(
        SUM(sales) * 100.0 /
        (SELECT SUM(sales) FROM superstore),
        2
    ) AS sales_percentage
FROM superstore
GROUP BY category
ORDER BY total_sales DESC;




SELECT
    region,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY region
ORDER BY total_sales DESC;

SELECT
    segment,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY segment
ORDER BY total_sales DESC;

SELECT
    region,
    category,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY region, category
ORDER BY region, total_sales DESC;


SELECT
    YEAR(order_date) AS year,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY YEAR(order_date)
ORDER BY year;


 SELECT
    MONTH(order_date) AS month,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY MONTH(order_date)
ORDER BY month;


 SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;


 SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;


SELECT
    customer_name,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 10;


 SELECT
    state,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY state
ORDER BY total_sales DESC
LIMIT 10;


 SELECT
    city,
    state,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY city, state
ORDER BY total_sales DESC
LIMIT 10;


 SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales,
    RANK() OVER (
        ORDER BY SUM(sales) DESC
    ) AS sales_rank
FROM superstore
GROUP BY product_name;


 SELECT
    category,
    product_name,
    ROUND(SUM(sales), 2) AS
    total_sales,
    RANK() OVER (
        PARTITION BY category
        ORDER BY SUM(sales) DESC
    ) AS category_rank
FROM superstore
Group By category,product_name
ORDER BY category,category_rank;


WITH customer_sales AS (
    SELECT
        customer_name,
        SUM(sales) AS total_sales
    FROM superstore
    GROUP BY customer_name
)
SELECT
    customer_name,
    ROUND(total_sales, 2) AS total_sales
FROM customer_sales
ORDER BY total_sales DESC
LIMIT 10;



SELECT
    customer_name,
    ROUND(SUM(sales), 2) AS total_sales,
    CASE
        WHEN SUM(sales) >= 10000 THEN 'High Value'
        WHEN SUM(sales) >= 5000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS customer_type
FROM superstore
GROUP BY customer_name
ORDER BY total_sales DESC;



 WITH region_category AS (
    SELECT
        region,
        category,
        SUM(sales) AS total_sales
    FROM superstore
    GROUP BY region, category
),
ranked AS (
    SELECT
        region,
        category,
        total_sales,
        RANK() OVER (
            PARTITION BY region
            ORDER BY total_sales DESC
        ) AS category_rank
    FROM region_category
)
SELECT
    region,
    category,
    ROUND(total_sales, 2) AS total_sales
FROM ranked
WHERE category_rank = 1;




SELECT
    product_name,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;


SELECT
    customer_name,
    ROUND(SUM(sales), 2) AS total_sales
FROM superstore
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 10;



SELECT
    category,
    ROUND(SUM(sales), 2) AS total_sales,
    RANK() OVER (
        ORDER BY SUM(sales) DESC
    ) AS category_rank
FROM superstore
GROUP BY category
ORDER BY category_rank;


WITH product_sales AS (
    SELECT
        category,
        product_name,
        SUM(sales) AS total_sales
    FROM superstore
    GROUP BY category, product_name
),
ranked_products AS (
    SELECT
        category,
        product_name,
        ROUND(total_sales, 2) AS total_sales,
        DENSE_RANK() OVER (
            PARTITION BY category
            ORDER BY total_sales DESC
        ) AS product_rank
    FROM product_sales
)
SELECT
    category,
    product_name,
    total_sales,
    product_rank
FROM ranked_products
WHERE product_rank <= 3
ORDER BY category, product_rank;


WITH monthly_sales AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        SUM(sales) AS total_sales
    FROM superstore
    GROUP BY YEAR(order_date), MONTH(order_date)
)
SELECT
    year,
    month,
    ROUND(total_sales, 2) AS total_sales
FROM monthly_sales
ORDER BY year, month;


WITH yearly_sales AS (
    SELECT
        YEAR(order_date) AS year,
        SUM(sales) AS total_sales
    FROM superstore
    GROUP BY YEAR(order_date)
),
sales_with_previous AS (
    SELECT
        year,
        total_sales,
        LAG(total_sales) OVER (
            ORDER BY year
        ) AS previous_year_sales
    FROM yearly_sales
)
SELECT
    year,
    ROUND(total_sales, 2) AS total_sales,
    ROUND(previous_year_sales, 2) AS previous_year_sales,
    ROUND(
        ((total_sales - previous_year_sales)
        / previous_year_sales) * 100,
        2
    ) AS growth_percentage
FROM sales_with_previous
ORDER BY year;





