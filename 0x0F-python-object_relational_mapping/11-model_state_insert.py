#!/usr/bin/python3
'''Insert a new state 'Louisiana' to the database'''

import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def insertState(conn, state_name):
    '''Prints the state given by param'''
    new_state = State()
    new_state.name = state_name
    conn.add(new_state)
    conn.commit()
    print(new_state.id)

if __name__ == "__main__":
    db = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                       .format(sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]),
                       pool_pre_ping=True)
    Base.metadata.create_all(db)

    Session = sessionmaker(db)
    connection = Session()

    insertState(connection, 'Louisiana')

    connection.close()
