# Write your MySQL query statement below
SELECT Visits.customer_id, COUNT(Visits.customer_id) as count_no_trans
FROM Visits
LEFT JOIN Transactions on Visits.visit_id = Transactions.visit_id
WHERE Transactions.amount is null
GROUP BY Visits.customer_id