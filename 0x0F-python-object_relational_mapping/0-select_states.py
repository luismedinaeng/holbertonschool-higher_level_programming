#!/usr/bin/python3
''' Script that lists all states from the database hbtn_0e_0_usa'''


def getStates(cursor):
    ''' Get the states of a database
    The cursor that would be used is inserted by param'''
    strsql = "SELECT * FROM states ORDER BY id"
    cursor.execute(strsql)
    states = cursor.fetchall()
    for state in states:
        print(state)

if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        print("Incorrect number of args")

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()

    getStates(cur)

    cur.close()
    db.close()
