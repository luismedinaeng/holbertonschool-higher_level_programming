#!/usr/bin/python3
'''Takes the name of a states as an argument and lists all cities of it'''


def getCitiesbyState(cursor, state_name):
    '''Get the cities of the state inserted by parameter
    Stablish the connect by the cursor inserted by param'''
    strsql = """SELECT cities.name
    FROM cities INNER JOIN states ON cities.state_id = states.id
    WHERE states.name=%s
    ORDER BY cities.id ASC"""

    count = cur.execute(strsql, (state_name, ))
    cities = cur.fetchall()
    for i, city in zip(range(count), cities):
        print(city[0], end='\n' if i == count - 1 else ', ')

if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 5:
        print("Invalid number of args")

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()

    getCitiesbyState(cur, sys.argv[4])

    cur.close()
    db.close()
