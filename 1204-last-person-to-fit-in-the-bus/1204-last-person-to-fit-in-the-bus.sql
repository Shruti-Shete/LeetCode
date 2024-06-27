# Write your MySQL query statement below

With Temp as
(Select turn, person_id, person_name, weight, sum(weight) over (order by turn) as Total 
from queue)
Select person_name from temp
where Total <= 1000
order by Total Desc limit 1




  
