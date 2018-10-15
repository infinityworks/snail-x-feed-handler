import os

URLS = {
    'auth': '/auth/token',
    'rounds': '/rounds',
    'races': '/races',
    'snails': '/snails',
    'results': '/results'
}

DB = {
    'host': "localhost",
    'user': "root",
    'password': "psqlpass",
    'database': "snailRacing",
    'port': "5432"
}

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-coded-key-pls-change'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://' + DB['user'] + ':' + DB[
        'password'] + '@' + DB['host'] + ':' + DB['port']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
