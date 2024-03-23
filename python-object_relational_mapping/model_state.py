#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """State clasd"""

    __tablename__ = "states"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)