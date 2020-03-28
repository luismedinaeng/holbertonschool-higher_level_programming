#!/usr/bin/python3
'''Takes the name of a states as an argument and lists all cities of that state'''

if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 5:
        print("Invalid number of args")

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()

    strsql="""SELECT cities.name
    FROM cities INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id"""

    count = cur.execute(strsql, (sys.argv[4], ))
    cities = cur.fetchall()

    for i, city in zip(range(count),cities):
        print(city[0], end='\n' if i == count - 1 else ', ')

    cur.close()
    db.close()
