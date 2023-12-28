# Write your MySQL query statement below
select m.name from Employee e 
inner join Employee m on e.managerId = m.id
group by e.managerId
Having count(e.id)>=5