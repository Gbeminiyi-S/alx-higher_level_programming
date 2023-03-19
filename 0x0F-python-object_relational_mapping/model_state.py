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

    path = sys.argv
    engine = create_engine(f"mysql+mysqldb://{path[1]}:{path[2]}@localhost/{path[3]}")

    Base.metadata.create_all(engine)
