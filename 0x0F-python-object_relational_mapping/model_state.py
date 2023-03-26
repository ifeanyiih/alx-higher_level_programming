#!/usr/bin/python3
"""a python file that contains the class definition of a
State and an instance Base = declarative_base()"""

from sqlalchemy.orm import declarative_state
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """declares the state table"""
    __tablename___ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
