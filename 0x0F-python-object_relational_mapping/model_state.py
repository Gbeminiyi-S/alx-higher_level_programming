#!/usr/bin/python3
""" Defines a class 'State'"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()


class State(Base):
    """Creates a column in the table"""
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Create an engine that connects to MySQL
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}\
            :{sys.argv[2]}@localhost/{sys.argv[3]}")

    # Create the tables in the database
    Base.metadata.create_all(engine)
