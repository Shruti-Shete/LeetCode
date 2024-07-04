# Write your MySQL query statement below


Select round(sum(i1.tiv_2016),2) as tiv_2016
from Insurance i1 where 
tiv_2015 in (
    Select tiv_2015
    from Insurance i2 
    where i1.pid != i2.pid)
AND (lat,lon) Not in (
Select lat,lon
    from Insurance i2 
    where i1.pid != i2.pid)


