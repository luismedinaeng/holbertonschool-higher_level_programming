#!/usr/bin/python3
'''Deletes all State objects containing an 'a' in its name'''

import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def deleteStates(conn):
    '''Delete states containing 'a' in its name'''
    query = conn.query(State).filter(State.name.like("%a%"))
    states = query.all()
    for state in states:
        conn.delete(state)

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

    deleteStates(connection)

    connection.close()
