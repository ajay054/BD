WITH SalesPayments AS (
SELECT
	fs.order_number,
	fs.order_date,
	fs.product_number,
	fs.line_item_payment
FROM
	fact_sales fs
JOIN
	dim_payments dp
ON
	fs.order_number = dp.order_number
)
SELECT
	order_number,
	order_date,
	product_number,
	line_item_payment,
	RANK() OVER (PARTITION BY product_number ORDER BY line_item_payment DESC) AS ranking
FROM 
	SalesPayments;