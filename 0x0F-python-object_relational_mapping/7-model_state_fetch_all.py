#!/usr/bin/python3
"""Script that prints all the records on the database
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


def getStates(conn):
    ''' Prints the list of the states
    connection i sthe actual session to the database'''
    query = conn.query(State.id, State.name).order_by(State.id)
    for st_id, st_name in query.all():
        print("{:d}: {:s}".format(st_id, st_name))


if __name__ == "__main__":
    db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]),
                       pool_pre_ping=True)
    Base.metadata.create_all(db)

    Session = sessionmaker(db)
    connection = Session()

    getStates(connection)

    connection.close()
