#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
import sqlalchemy
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    connector = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(connector.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Base.metadata.bind = engine
    Session = sessionmaker()
    Session.bind = engine
    session = Session()
    rows = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id).all()
    for state, city in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
        session.close()
