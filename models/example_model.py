from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, relation

from models import Base


class Example(Base):
    __tablename__ = 'example'
    id = Column(Integer, primary_key=True)
    column1 = Column(String(80), unique=True, nullable=False)
    column2 = Column(String(120), unique=True, nullable=False)

    # this is ORM (very different from the actual table cols, It uses class name instead of table name)
    children = relationship("Child")

    def __repr__(self):
        return '<Example %r>' % self.column1


class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    column1 = Column(String(80), unique=True, nullable=False)
    column2 = Column(String(120), unique=True, nullable=False)
    parent_id = Column(Integer, ForeignKey("parent.id"))

    parent = relation('Example')

    def __repr__(self):
        return '<Example %r>' % self.column1
