import sqlite3
from importlib import import_module

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker


class DBSessionProvider:
    url = None
    engine = None
    session_maker = None
    settings = None
    models_package = None

    @classmethod
    def get_session(cls) -> Session:
        return cls.session_maker()

    @staticmethod
    def __get_module():
        models_package = DBSessionProvider.settings['sqlalchemy']['models_package']
        return import_module('%s.%s' % (models_package, 'models'))

    @classmethod
    def read(cls, settings):
        cls.url = settings['sqlalchemy']['url']
        cls.engine = create_engine(cls.url)
        cls.session_maker = sessionmaker(bind=cls.engine, autoflush=False)
        if 'squile' in cls.url:
            sqlite3.connect(cls.url.split('///')[-1])
        cls.models_package = settings['sqlalchemy']['models_package']

    @classmethod
    def create_tables(cls):
        m = import_module('%s.%s' % (cls.models_package, 'models'))
        base = getattr(m, 'Base')
        base.metadata.create_all(cls.engine)
