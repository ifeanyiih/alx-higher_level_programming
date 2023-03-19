#!/usr/bin/python3

"""
This module contains a script that lists all states from the database
hbtn_0e_0_usa based on a users input
"""

import MySQLdb
import sys


def listStates(uname, passwd, dbname, uinput):
    """Creates a connection to a database and lists the states
    from database hbtn_0e_0_usa

    Args:
        uname (str): username
        passwd (str): password
        dbname (str): database to access
        uinput (str): user input
    Returns:
        None
    """
    db = MySQLdb.connect(host="localhost", user=uname,
                         passwd=passwd, db=dbname, port=3306)
    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE"
                " name LIKE '{}%' ORDER BY states.id ASC".format(uinput))
    rows = cur.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    uname, passwd, dbname, uinput = sys.argv[1:]
    listStates(uname, passwd, dbname, uinput)
