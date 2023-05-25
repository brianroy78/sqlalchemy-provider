import os
from configparser import ConfigParser
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.future import Engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Data:
    URL: str
    ENGINE: Optional[Engine]
    SESSION_MAKER: Optional[sessionmaker]


def set_settings(url: str):
    Data.URL = url
    Data.ENGINE = create_engine(url)
    Data.SESSION_MAKER = sessionmaker(bind=Data.ENGINE)


def get_session() -> Session:
    assert Data.SESSION_MAKER is not None
    return Data.SESSION_MAKER()


def connect():
    from database._table_registration import tables

    set_settings(_get_settings()["sqlalchemy.url"])


def connect_get_session():
    connect()
    return get_session()


def create_database():
    connect()
    Base.metadata.create_all(Data.ENGINE)


def remove_sqlite_db():
    os.remove(_get_settings()["sqlalchemy.url"].split("/")[-1])


def _get_settings():
    config = ConfigParser()
    config.read("settings.ini")
    return config["database"]
