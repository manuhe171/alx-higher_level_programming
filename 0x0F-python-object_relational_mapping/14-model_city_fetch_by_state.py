#!/usr/bin/python3
'''script that athat prints all City objects from the database hbtn_0e_14_usa
Your code should not be executed when imported'''

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    city = session.query(City, State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id).all()
    for c, s in city:
        print('{}: ({}) {}'.format(s.name, c.id, c.name))
