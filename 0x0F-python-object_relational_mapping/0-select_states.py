#!/usr/bin/python3


"""
lists all states from the database hbtn_0e_0_usa
 script should take 3 arguments: mysql username, mysql password and db name
 Before you run the script execute: cat 0-select_states.sql | mysql -uroot -p
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to a database
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])

    # create a cursor to exec queries using SQL
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
