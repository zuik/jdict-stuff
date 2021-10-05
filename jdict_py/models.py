"""
models.py - SQLAlchemy models for the Jdict database

We will follow roughly how JMdict is organized.
"""
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Entry(Base):
    """
    A word entry
    """

    __tablename__ = "entries"

    entry_id = Column(Integer, primary_key=True)
    reading_el = Column(String)
    kanji_el = Column(String)
    sense = Column(String)

    @staticmethod
    def new_entry(reading_el: str, kanji_el: str, sense: str):
        """
        Create a new entry
        """
        return Entry(reading_el=reading_el, kanji_el=kanji_el, sense=sense)

    def __repr__(self):
        return f"<Entry(entry_id={self.entry_id}, reading_el={self.reading_el}, kanji_el={self.kanji_el}, sense={self.sense})>"

    def to_dict(self):
        """
        Return a dictionary representation of this object
        """
        return {
            "entry_id": self.entry_id,
            "reading_el": self.reading_el,
            "kanji_el": self.kanji_el,
            "sense": self.sense,
        }
