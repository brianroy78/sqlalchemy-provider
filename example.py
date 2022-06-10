from configparser import ConfigParser

from models import set_settings, Base, Data

config = ConfigParser()
config.read('settings.ini')
set_settings(config['DEFAULT']['sqlalchemy.url'])

# this will create the database
Base.metadata.create_all(Data.ENGINE)
