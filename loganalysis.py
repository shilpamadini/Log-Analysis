#!/usr/bin/env python


# "Database code" for Log analysis from news reporting.

import psycopg2

db_name = "news"

# Connect to database

try:
    db = psycopg2.connect(database=db_name)
except psycopg2.Error as e:
    print("Unable to connect to the database.")
    print(e.diag.message_primary)
    print("                                  ")
else:
    print("Connected to {} database.".format('news'))
    print("                                  ")
    c = db.cursor()

    # Select most popular three articles of all time.
    # Code uses a view title_logs that is predefined in database.

    sql_query = "select title,count(ip) as cnt from title_logs \
                group by title order by cnt desc limit 3"
    try:
        c.execute(sql_query)
    except psycopg2.Error as e:
        print(e.diag.message_primary)
        print("                                  ")
    else:
        rows = c.fetchall()
        print('The most popular three articles of all time.')
        print('-------------------------------------------')
        for row in rows:
            print('"{}" - {} views'.format(row[0], row[1]))
        print("                                  ")

    # Select most popular article authors of all time.
    # Code uses a view title_logs that is predefined in database.

    sql_query = "select a.name,s.cnt as count from \
                authors a, \
                (select author, count(ip) as cnt from title_logs \
                group by author) s where a.id = s.author order by count desc"
    try:
        c.execute(sql_query)
    except psycopg2.Error as e:
        print(e.diag.message_primary)
        print("                                  ")
    else:
        rows = c.fetchall()
        print('The most popular authors of all time.')
        print('-------------------------------------------')
        for row in rows:
            print('"{}" - {} views'.format(row[0], row[1]))
        print("                                  ")

    # Select the days when more than 1% of the requests led to error.
    # Code uses a view log_req_prcnt that is predefined in database.

    sql_query = "select to_char(date,'MON DD,YYYY'),round(percentage,2) as per from \
                log_req_prcnt where percentage>1 and status = '404 NOT FOUND'\
                "
    try:
        c.execute(sql_query)
    except psycopg2.Error as e:
        print(e.diag.message_primary)
        print("                                  ")
    else:
        rows = c.fetchall()
        print('The days when more than 1''%'' \
of requests lead to errors')
        print('-------------------------------------------')
        for row in rows:
            print('{} - {}''%'' errors'.format(row[0], row[1]))
            print("                                  ")
