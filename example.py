from configparser import ConfigParser

from models import set_settings, Base, Data
from models.example_model import *  # it's better to import all

config = ConfigParser()
config.read('settings.ini')
set_settings(config['DEFAULT']['sqlalchemy.url'])

# this will create the database

Base.metadata.create_all(Data.ENGINE)
