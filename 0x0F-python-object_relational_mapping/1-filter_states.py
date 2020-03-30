#!/usr/bin/python3
''' Script that lists states starting with 'N' from database hbtn_0e_0_usa'''

import sys
import MySQLdb


def getStatesStartingN(cursor):
    ''' Get the states of a database that starts with 'N'
    The cursor that would be used is inserted by param'''
    strsql = "SELECT * FROM states WHERE name LIKE %s ORDER BY id"
    cursor.execute(strsql, ('N%',))
    states = cursor.fetchall()
    for state in states:
        print(state)

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()

    getStatesStartingN(cur)

    cur.close()
    db.close()
