class DBSessionProvider:
    session_maker = None
    connection_string = 'sqlite:///scraping.db'

    @staticmethod
    def get_session() -> Session:
        if DBSessionProvider.session_maker is None:
            engine = create_engine(DBSessionProvider.connection_string)
            sqlite3.connect(DBSessionProvider.connection_string.split('///')[-1])
            Base.metadata.create_all(engine, checkfirst=True)
            DBSessionProvider.session_maker = sessionmaker(bind=engine, autoflush=False)
        return DBSessionProvider.session_maker()
