#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""
import sqlalchemy
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

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
