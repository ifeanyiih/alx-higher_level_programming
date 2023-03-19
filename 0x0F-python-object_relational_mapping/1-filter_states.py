#!/usr/bin/python3

"""
This module contains a script that lists all states from the database
hbtn_0e_0_usa.
"""

import MySQLdb
import sys


def listStates(uname, passwd, dbname):
    """Creates a connection to a database and lists the states
    from database hbtn_0e_0_usa

    Args:
        uname (str): username
        passwd (str): password
        dbname (str): database to access
    Returns:
        None
    """
    db = MySQLdb.connect(host="localhost", user=uname,
                         passwd=passwd, db=dbname, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    uname, passwd, dbname = sys.argv[1:]
    listStates(uname, passwd, dbname)
