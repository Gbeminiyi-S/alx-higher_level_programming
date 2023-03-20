#!/usr/bin/python3
""" a script that adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all the tables associated with the Base metadata
    Base.metadata.create_all(engine)

    # Create a new Session instance bound to the engine we created
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add thw State Object
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
