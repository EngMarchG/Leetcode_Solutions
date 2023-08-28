# Write your MySQL query statement below
SELECT
    pr.product_id,
    ROUND(SUM(pr.price*us.units) / SUM(us.units), 2) as average_price
FROM
    Prices pr
CROSS JOIN
    UnitsSold us on pr.product_id = us.product_id 
    AND us.purchase_date BETWEEN pr.start_date AND pr.end_date
GROUP BY
    pr.product_id


