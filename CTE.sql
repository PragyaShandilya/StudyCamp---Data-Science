
WITH highest_sal AS (
    SELECT name, salary
    FROM employee
    ORDER BY salary DESC
    LIMIT 2
)
SELECT name, salary
FROM highest_sal
WHERE salary != (SELECT MAX(salary) FROM highest_sal)