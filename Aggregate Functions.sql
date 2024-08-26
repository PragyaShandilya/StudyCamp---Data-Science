#Question: Find the average salary of employees in the employees table.
select avg(salary) from employee;

#Question: Count the number of employees in each department.
SELECT dept, COUNT(*) FROM employee
GROUP BY dept;

#Question: Retrieve employee names and their corresponding department names.
select name, dept from employee;

#Question: Retrieve the names of employees who have a salary higher than the average
#salary.
select name from employee
where salary > 74000;