#!/usr/bin/python3

"""
This module takes the name of a state as an argument and lists all cities
of that state using the database hbtn_0e_4_usa
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
    cur.execute(f"SELECT cities.name FROM cities"
                " WHERE cities.state_id = "
                f"(SELECT id FROM states WHERE states.name LIKE '{uinput}%')")
    rows = cur.fetchall()
    arr = []
    for row in rows:
        arr.append(row[0])
    print(', '.join(arr))


if __name__ == "__main__":
    uname, passwd, dbname, uinput = sys.argv[1:]
    uinput = uinput.strip("';*= ")
    listStates(uname, passwd, dbname, uinput)
