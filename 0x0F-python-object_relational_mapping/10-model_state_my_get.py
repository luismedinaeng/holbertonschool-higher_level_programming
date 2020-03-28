#!/usr/bin/python3
'''Prints the state id with the name passed as argumnet'''

import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def getState(conn, state_name):
    '''Prints the state given by param'''
    query = conn.query(State.id).filter(State.name == state_name)
    try:
        print(query.one()[0])
    except:
        print("Not found")

if __name__ == "__main__":
    db = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                       .format(sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]),
                       pool_pre_ping=True)
    Base.metadata.create_all(db)

    Session = sessionmaker(db)
    connection = Session()

    getState(connection, sys.argv[4])

    connection.close()
