#!/usr/bin/python3
''' Module that has the definition of an State instance'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    '''Class that represents a state'''
    __tablename__ = 'states'

    id = Column('id', Integer, primary_key=True, nullable=False,
                autoincrement=True, unique=True)
    name = Column('name', String(128), nullable=False)

    cities = relationship("City", backref="state", order_by="City.id")
