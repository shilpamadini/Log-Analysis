--Create view sql for title_logs

create view title_logs as
(select ar.author,ar.title,ar.slug,lg.path,lg.ip,lg.method,lg.status,lg.time,lg.id from articles ar , log lg
where lg.path = concat('/article/',ar.slug) order by ar.title);
