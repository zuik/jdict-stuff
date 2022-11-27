"""
models.py - SQLAlchemy models for the Jdict database

We will follow roughly how JMdict is organized.
"""
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.dialects import postgresql as pg

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Entry(Base):
    """
    A word entry
    """

    __tablename__ = "entries"

    entry_id = Column(Integer, primary_key=True)
    jdict_entry_id = Column(Integer)

    kanji = Column(String)
    reading = Column(String)

    senses = Column(pg.JSONB)
    meta = Column(pg.JSONB)

    @staticmethod
    def new_entry(jdict_entry_id, reading, senses, kanji=None, meta=None):
        """
        Create a new entry
        """
        return Entry(
            jdict_entry_id=jdict_entry_id,
            reading=reading,
            senses=senses,
            kanji=kanji,
            meta=meta,
        )

    def __repr__(self):
        return f"<Entry(entry_id={self.entry_id} reading={self.reading} kanji={self.kanji}>"

    def to_dict(self):
        """
        Return a dictionary representation of this object
        """
        return {
            "entry_id": self.entry_id,
            "jdict_entry_id": self.jdict_entry_id,
            "kanji": self.kanji,
            "reading": self.reading,
            "senses": self.senses,
            "meta": self.meta,
        }

if __name__ == "__main__":
    from sqlalchemy import create_engine


    engine = create_engine("postgresql+psycopg2://postgres:minhdang@localhost:35432/postgres", echo=True)

    Base.metadata.create_all(engine)