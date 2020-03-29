#!/usr/bin/python3
'''Creates a new state with an associated city'''
import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def createCascadeRecord(conn):
    '''Creates a new state with an associated city'''
    state = State(name='California')
    state.cities = [City(name='San Francisco')]
    conn.add(state)
    conn.commit()


if __name__ == "__main__":
    db = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                       .format(sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]),
                       pool_pre_ping=True)
    Base.metadata.create_all(db)

    Session = sessionmaker(db)
    connection = Session()

    createCascadeRecord(connection)

    connection.close()
