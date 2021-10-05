"""
models.py - SQLAlchemy models for the Jdict database

We will follow roughly how JMdict is organized.
"""
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Entry(Base):
    """
    A word entry
    """
