from sqlalchemy import Column, Integer, String

from models import Base


class Example(Base):
    __tablename__ = 'example'
    id = Column(Integer, primary_key=True)
    column1 = Column(String(80), unique=True, nullable=False)
    column2 = Column(String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Example %r>' % self.column1
