#!/usr/bin/python3
'''python file that contains the class definition of a State
and an instance Base = declarative_base()'''

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format('root', 'root', 'hbtn_0e_6_usa'),
                       pool_pre_ping=True)


class State(Base):
    '''CLass State'''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
