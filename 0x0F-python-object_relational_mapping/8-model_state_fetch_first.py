#!/usr/bin/python3
'''Script that prnts the first State object of the database
'''
import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def getFirstState(conn):
    '''Prints the first state of the database
    If not state is found, print Nothing'''
    query = conn.query(State.id, State.name).order_by(State.id)
    try:
        (st_id, st_name) = query.first()
        print("{:d}: {:s}".format(st_id, st_name))
    except:
        print("Nothing")

if __name__ == "__main__":
    db = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]),
                       pool_pre_ping=True)
    Base.metadata.create_all(db)

    Session = sessionmaker(db)
    connection = Session()

    getFirstState(connection)

    connection.close()
