import sqlalchemy as sa
from sqlalchemy import orm
from datetime import datetime

from database import Base


class Example(Base):
    __tablename__ = "example"
    id = sa.Column(sa.Integer, primary_key=True)
    column1 = sa.Column(sa.String(80), unique=True, nullable=False)
    column2 = sa.Column(sa.String(120), unique=True, nullable=False)
    created_at = sa.Column(sa.DateTime, default=datetime.now)
    updated_at = sa.Column(sa.DateTime, default=datetime.now, onupdate=datetime.now)

    children = orm.relationship("Child")

    def __repr__(self):
        return "<Example %r>" % self.column1


class Child(Base):
    __tablename__ = "child"
    id = sa.Column(sa.Integer, primary_key=True)
    column1 = sa.Column(sa.String(80), unique=True, nullable=False)
    column2 = sa.Column(sa.String(120), unique=True, nullable=False)
    parent_id = sa.Column(sa.Integer, sa.ForeignKey("example.id"))

    parent = orm.relationship("Example")

    def __repr__(self):
        return "<Example %r>" % self.column1
