#!/usr/bin/python3

"""
This module contains a script that lists all cities from the database
"""

import MySQLdb
import sys


def listStates(uname, passwd, dbname):
    """Creates a connection to a database and lists the cities
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
    cur.execute(f"SELECT cities.id, cities.name AS city,"
                f" states.name AS state FROM states INNER JOIN cities"
                " WHERE states.id=cities.state_id"
                " ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    uname, passwd, dbname = sys.argv[1:]
    listStates(uname, passwd, dbname)
