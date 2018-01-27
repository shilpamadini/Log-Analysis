#!/usr/bin/env python
"""Python database code for reporting from news database."""

import psycopg2
import sys

db_name = "news"

# Connect to database

try:
    db = psycopg2.connect(database=db_name)
except psycopg2.OperationalError as e:
    print(str(e)+"\n")
    sys.exit(1)
else:
    print("Connected to {} database.".format('news')+"\n")
    c = db.cursor()

sql_1 = "select title,count(ip) as cnt from title_logs \
            group by title order by cnt desc limit 3"
sql_2 = "select a.name,s.cnt as count from \
            authors a, \
            (select author, count(ip) as cnt from title_logs \
            group by author) s where a.id = s.author order by count desc"
sql_3 = "select to_char(date,'MON DD,YYYY'),round(percentage,2) as per from \
            log_req_prcnt where percentage>1 and status = '404 NOT FOUND'"


def get_report(input_query):
    """Function to exeute and return the results of a sql statement."""
    try:
        c.execute(input_query)
    except psycopg2.Error as e:
        print(e.diag.message_primary+"\n")
        sys.exit(1)
    else:
        rows = c.fetchall()
        return rows


# Select most popular three articles of all time.
# Code uses a view title_logs that is predefined in database.

# print('\033[4mThe most popular three articles of all time\033[0m')
print('The most popular three articles of all time')
print('-------------------------------------------')
records = get_report(sql_1)
for rec in records:
    print('"{}" - {} views'.format(rec[0], rec[1]))
print("\n")

# Select most popular article authors of all time.
# Code uses a view title_logs that is predefined in database.

print('The most popular authors of all time')
print('-------------------------------------------')
records = get_report(sql_2)
for rec in records:
    print('"{}" - {} views'.format(rec[0], rec[1]))
print("\n")

# Select the days when more than 1% of the requests led to error.
# Code uses a view log_req_prcnt that is predefined in database.

print('The days when more than 1''%'' \
of requests lead to errors')
print('-------------------------------------------')
records = get_report(sql_3)
for rec in records:
    print('{} - {}''%'' errors'.format(rec[0], rec[1]))
print("\n")

# close the cursor

c.close()

# close the database connection

db.close()
