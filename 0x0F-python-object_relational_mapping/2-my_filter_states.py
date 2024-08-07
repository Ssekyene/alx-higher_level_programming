#!/usr/bin/python3
"""
The script takes an arg & displays all values in the states table where name
matches the arg
script takes 4 arguments: username, password, db name and state name searched
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
    sql_cmd = """SELECT *
                 FROM states
                 WHERE name LIKE '{:s}'
                 ORDER BY id ASC""".format(argv[4])
    cur.execute(sql_cmd)
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == argv[4]:
            print(row)
    cur.close()
    conn.close()
