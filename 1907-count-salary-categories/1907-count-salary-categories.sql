# Write your MySQL query statement below
Select "High Salary" as category, sum(case When income > 50000 then 1 else 0 end) as accounts_count
From Accounts
union
Select "Low Salary" as category, sum(case When income < 20000 then 1 else 0 end) as accounts_count
From Accounts
union
Select "Average Salary" as category, sum(case When income between 20000 and 50000 then 1 else 0 end) as accounts_count
From Accounts;







 


