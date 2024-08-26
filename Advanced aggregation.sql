#Question: Find the top three departments with the highest total salaries.
select dept, sum(salary) as total_salary from employee
group by dept
order by total_salary desc
limit 3;