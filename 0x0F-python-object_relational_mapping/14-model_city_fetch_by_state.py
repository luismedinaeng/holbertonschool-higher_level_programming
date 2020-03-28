#!/usr/bin/python3
'''Script that prints all the cities in the database'''

import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def getCities(conn):
    '''Prints all the cities with them states'''
    query = conn.query(City).order_by(City.id)
    cities = query.all()
    for city in cities:
        print("{}: ({:d}) {}".format(city.state.name, city.id, city.name))

if __name__ == "__main__":
    db = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                       .format(sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]),
                       pool_pre_ping=True)
    Base.metadata.create_all(db)

    Session = sessionmaker(db)
    connection = Session()

    getCities(connection)

    connection.close()
