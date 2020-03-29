#!/usr/bin/python3
'''Creates a new state with an associated city'''
import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def listStatesCities(conn):
    '''Creates a new state with an associated city'''
    query = conn.query(State).order_by(State.id)
    states = query.all()
    for state in states:
        print("{:d}: {:s}".format(state.id, state.name))
        for city in state.cities:
            print("\t{:d}: {:s}".format(city.id, city.name))


if __name__ == "__main__":
    db = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                       .format(sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]),
                       pool_pre_ping=True)
    Base.metadata.create_all(db)

    Session = sessionmaker(db)
    connection = Session()

    listStatesCities(connection)

    connection.close()
