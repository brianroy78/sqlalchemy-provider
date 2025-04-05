import sqlalchemy as sa
from sqlalchemy import orm

import settings


class Data:
    URL: str | None
    ENGINE: sa.Engine | None
    SESSION_MAKER: orm.sessionmaker | None


def get_session() -> orm.Session:
    if not Data.URL:
        Data.URL = settings.DB_URL
        Data.ENGINE = sa.create_engine(url=Data.URL)
        Data.SESSION_MAKER = orm.sessionmaker(bind=Data.ENGINE)

    assert Data.SESSION_MAKER is not None
    return Data.SESSION_MAKER()
