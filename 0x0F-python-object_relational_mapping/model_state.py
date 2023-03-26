#!/usr/bin/python3
"""Write a python file that contains the class definition of a State
and an instance Base = declarative_base():
State class:
inherits from Base Tips
links to the MySQL table states
class attribute id that represents a column of an auto-generated,
unique integer, cannot be null and is a primary key
class attribute name that represents a column of a string
with maximum 128 characters and cannot be null
WARNING: all classes who inherit from Base must be imported
before calling Base.metadata.create_all(engine)
"""

from sqlalchemy.orm import declarative_state
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """Declares the state table
    State Class that inherits from base linking to the states table
    class attribute id that represents a column of an auto-generated,
    unique integer, can't be null and is a primary key
    class attribute name that represents a column of a string
    with maximum 128 characters and can't be null

    Attributes:
        id (int): the class attribute
        name (str): class attribute
    """
    __tablename___ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
