#!/usr/bin/python3
'''Lists all State that contain the letter a'''

import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def getStatesWitha(conn):
    '''Prints every state that contains the 'a' char'''
    query = conn.query(State).filter(State.name.like('%a%')).order_by(State.id)
    states = query.all()
    for state in states:
        print("{:d}: {:s}".format(state.id, state.name))

if __name__ == "__main__":
    db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]),
                       pool_pre_ping=True)
    Base.metadata.create_all(db)

    Session = sessionmaker(db)
    connection = Session()

    getStatesWitha(connection)

    connection.close()
