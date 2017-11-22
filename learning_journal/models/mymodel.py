"""This is the docstring in my model."""
from sqlalchemy import (
    Column,
    DateTime,
    Index,
    Integer,
    Text,
    Unicode
)

from .meta import Base


class Journal(Base):
    """Class for mymodel."""
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    creation_date = Column(DateTime)

    def to_dict(self):
        """."""
        return {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'creation_date': self.created.strftime('%Y-%m-%d')
        }
