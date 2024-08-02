
with RankedSalaries as (
select name, department, salary, 
rank() over (partition by department order by salary)
from employees
)
select * from RankedSalaries where rank = 3;
