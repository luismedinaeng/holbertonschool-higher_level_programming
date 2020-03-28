#!/usr/bin/python3
'''Script that lists all cities from the database '''

if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        print("Incorrect number of args")

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    strsql = """SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id"""
    cur.execute(strsql)

    cities = cur.fetchall()

    for city in cities:
        print(city)

    cur.close()
    db.close()
