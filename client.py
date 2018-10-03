from configparser import ConfigParser

from provider import DBSessionProvider


def main():
    config = ConfigParser()
    config.read('production.ini')
    DBSessionProvider.read(config)
    DBSessionProvider.create_tables()


if __name__ == '__main__':
    main()
