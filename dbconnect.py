#!/usr/bin/env python
"""Python code to create DBHandler class."""

import psycopg2
import sys


class DBHandler():
    """
    This class provides blueprint to connect to database
    and execute statements.
    """

    def __init__(self, db_name, sql):
        """
        Constructor for the Dbconnet instance
        :param db_name: string
        :param sql: string
        """
        self.dbname = db_name
        self.sql_statement = sql

    def connect_db(self):
        """
        Function connects to database, executes the sql statement
        and returns results.
        """
        try:
            db = psycopg2.connect(database=self.dbname)
            cursor = db.cursor()
            cursor.execute(self.sql_statement)
            rows = cursor.fetchall()
            db.close()
            return rows
        except psycopg2.OperationalError as e:
            print(str(e)+"\n")
            sys.exit(1)
        except psycopg2.Error as e:
            print("verify your sql statement, "+e.diag.message_primary+"\n")
            sys.exit(1)
