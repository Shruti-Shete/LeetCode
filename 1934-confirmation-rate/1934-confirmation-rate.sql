# Write your MySQL query statement below

Select s.user_id , Case when c.time_stamp is null then 0.00
Else Round(Sum(c.action = "confirmed")/count(*), 2)
End as confirmation_rate
from Signups s Left join Confirmations c
on s.user_id = c.user_id
group by s.user_id
