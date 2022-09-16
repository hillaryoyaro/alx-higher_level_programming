#!/usr/bin/python3
""" Take in an argument and display all values
    in the states table of hbtn_0e_0_usa
    where name matches the argument
    and is safe from SQL Injections """

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
