#!/usr/bin/python3
""" a script that changes the name of a State object
    from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # Create all the tables associated with the Base metadata
    Base.metadata.create_all(engine)

    # Create a new Session instance bound to the engine we created
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object from the database and update value
    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()
