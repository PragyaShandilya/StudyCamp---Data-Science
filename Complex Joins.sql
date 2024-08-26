#Question: Retrieve the names of employees and their managers (use self-join).

select e.name as employee, m.manager as manager
from employee as e 
join employee as m 
on e.name = m.name;


#Question: Retrieve the salaries of employees along with the average salary of their
#department.
select e.name, e.salary, avg(e.salary) as average_salary
from employee as e
join employee as d 
on e.name = d.name
group by e.dept, e.name, e.salary;