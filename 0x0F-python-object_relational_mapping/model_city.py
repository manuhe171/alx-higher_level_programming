#!/usr/bin/python3
'''python file that contains the class definition of a City'''

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import sys
from model_state import Base, State

Base = declarative_base()


class City(Base):
    '''Class City'''

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
