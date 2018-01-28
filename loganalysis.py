#!/usr/bin/env python
"""Python database code for reporting from news database."""

import dbconnect

db_name = "news"
sql_1 = "select title,count(ip) as cnt from title_logs \
            group by title order by cnt desc limit 3"
sql_2 = "select a.name,s.cnt as count from \
            authors a,(select author, count(ip) as cnt from title_logs \
            group by author) s where a.id = s.author order by count desc"
sql_3 = "select to_char(date,'MON DD,YYYY'),round(percentage,2) as per from \
            log_req_prcnt where percentage>1 and status = '404 NOT FOUND'"

title_1 = "The most popular three articles of all time"
title_2 = "The most popular authors of all time"
title_3 = "The days when more than 1% \
of requests lead to errors"


def print_report(qt, sign, title, rows, txt):
    """Function to print out the reports in text format."""
    print(title)
    print('-------------------------------------------')
    for rec in rows:
        print('{}{}{} - {}{} {}'.format(qt, rec[0], qt, rec[1], sign, txt))
    print("\n")


if __name__ == '__main__':
    # Create instances of dbconnect

    report_1 = dbconnect.Connect(db_name, sql_1)
    report_2 = dbconnect.Connect(db_name, sql_2)
    report_3 = dbconnect.Connect(db_name, sql_3)

    # Call connect_db method of class Connect for all the instances

    record_1 = report_1.connect_db()
    record_2 = report_2.connect_db()
    record_3 = report_3.connect_db()

    # Print reports
    # Select most popular three articles of all time.
    print_report('"', '', title_1, record_1, 'views')
    # Select most popular article authors of all time.
    print_report('', '', title_2, record_2, 'views')
    # Select the days when more than 1% of the requests led to error.
    print_report('', "%", title_3, record_3, 'errors')
