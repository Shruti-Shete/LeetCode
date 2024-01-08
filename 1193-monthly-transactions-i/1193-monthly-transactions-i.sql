Select date_format(trans_date, '%Y-%m') as month, country , count(id) as trans_count, count(case when state = "approved" then id End) as approved_count , Sum(amount) as trans_total_amount,
Coalesce(Sum(case when state = "approved" then amount End),0) as approved_total_amount
from Transactions
group by country, month;
