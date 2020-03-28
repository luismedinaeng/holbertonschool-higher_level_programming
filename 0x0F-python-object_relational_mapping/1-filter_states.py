#!/usr/bin/python3
''' Script that lists states starting with 'N' from the database hbtn_0e_0_usa'''

if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        print("Incorrect number of args")

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)

    cur.close()
    db.close()
