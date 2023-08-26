# Write your MySQL query statement below
SELECT f.id from Weather as f, Weather as s
WHERE Datediff(f.recordDate, s.recordDate ) = 1
&& f.temperature > s.temperature