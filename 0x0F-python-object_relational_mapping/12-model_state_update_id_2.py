#!/usr/bin/python3
'''Update the state with id 2 with 'New Mexico' name'''

import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def updateState(conn, state_id, new_name):
    '''Update the id state given by param with the name given'''
    state = conn.query(State).filter(State.id == state_id).one()
    state.name = new_name
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

    updateState(connection, 2, 'New Mexico')

    connection.close()
