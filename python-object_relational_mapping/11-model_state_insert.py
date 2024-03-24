#!/usr/bin/python3
"""a script that adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""
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
    """Creata a new state object"""
    new_state = State(name='Louisiana')

    """Add the new state to the session and commit to the database"""
    session.add(new_state)
    session.commit()
    print(new_state.id)
