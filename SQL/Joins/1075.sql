# Write your MySQL query statement below
SELECT
    p.project_id,
    ROUND(AVG(e.experience_years), 2) as average_years
FROM    
    Employee e
LEFT JOIN
    Project p on e.employee_id = p.employee_id
WHERE
    p.project_id is not null
GROUP BY
    p.project_id