#!/usr/bin/python3
"""
This Module contains a python file that contains the class definition of a
State and an instance Base = declarative_base().
This module would prove my understanding of a creating Objects
Maps using sqlalchemy.
"""

from sqlalchemy.orm import declarative_state
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """Declares the state table
    Attributes:
        id (int): the class attribute
        name (str): class attribute
    """
    __tablename___ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
