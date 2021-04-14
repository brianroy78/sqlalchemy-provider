from configparser import ConfigParser

from models import set_settings

config = ConfigParser()
config.read('settings.ini')
set_settings(config['DEFAULT']['sqlalchemy.url'])
