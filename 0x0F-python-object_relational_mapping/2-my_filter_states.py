#!/usr/bin/python3
''' Script that lists states that matches the argument
from the database hbtn_0e_0_usa'''
import sys
import MySQLdb


def getStates(cursor, state_name):
    ''' Get the states of a database that matches with the param
    The cursor that would be used is inserted by param'''
    strsql = """SELECT *
    FROM states
    WHERE BINARY name = '{}'
    ORDER BY id""".format(state_name)

    cursor.execute(strsql)
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

    getStates(cur, sys.argv[4])

    cur.close()
    db.close()
