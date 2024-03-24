#!/usr/bin/python3
""" a script that changes the name of a State object
from the database hbtn_0e_6_usa"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    """connect to the database"""
    connection = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    """create the SQLAlchemy engine"""
    engine = create_engine(connection)

    Base.metadata.create_all(engine)

    """creata a session"""
    session = Session(engine)
    state_to_update = session.query(State).filter(State.id == 2).first()

    """update the name if the state is found"""
    if state_to_update:
        state_to_update.name = 'New Mexico'
        session.commit()