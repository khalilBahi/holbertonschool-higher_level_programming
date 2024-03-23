#!/usr/bin/python3
"""script that prints the first State object
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
    """create a session to interact with the database"""
    session = Session(engine)
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f'{first_state.id}: {first_state.name}')
    else:
        print('Nothing')
