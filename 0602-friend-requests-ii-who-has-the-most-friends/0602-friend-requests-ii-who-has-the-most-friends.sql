# Write your MySQL query statement below

With all_id as (
    Select requester_id as id
     from RequestAccepted
    Union All
    Select accepter_id as id
    from RequestAccepted)
    
Select id, count(id) as num
from all_id
group by id
order by count(id) Desc 
limit 1