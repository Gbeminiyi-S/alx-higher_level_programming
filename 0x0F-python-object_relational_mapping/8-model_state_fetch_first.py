#!/usr/bin/python3
"""a script that prints the first State object from the database hbtn_0e_6_usa
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

    # Query the first State object from the database
    first_state = session.query(State).first()

    # Print the State objects in the format speciified
    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))

    session.close()
