SELECT
    e.name
FROM 
    Employee e
INNER JOIN
    (SELECT managerId, COUNT(*) as num_reports 
    FROM Employee 
    WHERE managerId <> id
    GROUP BY managerId
) rep ON e.id = rep.managerId
WHERE
    rep.num_reports >= 5 
