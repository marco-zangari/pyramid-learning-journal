from sqlalchemy import (
    Column,
    DateTime,
    Index,
    Integer,
    Text,
    Unicode
)

from .meta import Base


class MyModel(Base):
    """Class for mymodel."""
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode)
    body = Column(Unicode)
    creation_date = Column(DateTime)


Index('my_index', MyModel.name, unique=True, mysql_length=255)
