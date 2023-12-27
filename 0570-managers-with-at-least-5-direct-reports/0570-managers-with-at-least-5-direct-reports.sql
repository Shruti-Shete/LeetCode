# Write your MySQL query statement below
Select name from Employee where id IN
(Select managerId From Employee Group by managerId
having Count(Distinct(id)) >= 5) 
