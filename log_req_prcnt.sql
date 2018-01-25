-- Create view sql for log_req_prcnt

create view log_req_prcnt as
(
select s.date,s.method,s.status,
s.cnt_status,r.cnt_requests,(s.cnt_status * 100)::numeric/r.cnt_requests as percentage
from
(select method,status,time::date as date, count(status) as cnt_status
from log group by method,status,date order by date) s,
(select method,time::date as date ,count(method) as cnt_requests
from log group by method, date order by date) r
where s.method = r.method
and s.date = r.date
order by s.date
);
