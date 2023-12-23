# Write your MySQL query statement below
Select E.name, B.bonus from Employee E left Join Bonus B
on E.empId = B.empId
where bonus < 1000 or bonus is Null;