#!/usr/bin/python3
'''Creates a new state with an associated city'''
import sys
from relationship_state import Base, State
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                       .format(sys.argv[1],
                               sys.argv[2],
                               sys.argv[3]),
                       pool_pre_ping=True)

    Session = sessionmaker(db)
    conn = Session()

    cities = conn.query(City).order_by(City.id).all()
    for city in cities:
        print("{:d}: {:s} -> {:s}".format(city.id, city.name, city.state.name))

    conn.close()
