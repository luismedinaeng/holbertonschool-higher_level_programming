#!/usr/bin/python3
'''Script that lists all cities from the database '''


def getCitiesByStates(cursor):
    ''' Lists all cities with its state
    Takes the cursor by param to connect the database'''

    strsql = """SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id"""

    cursor.execute(strsql)

    cities = cursor.fetchall()
    for city in cities:
        print(city)

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

    getCitiesByStates(cur)

    cur.close()
    db.close()
