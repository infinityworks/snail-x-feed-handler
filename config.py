import os

URLS = {
    'auth': 'https://dev-snailx-api.herokuapp.com//auth/token',
    'rounds': 'https://dev-snailx-api.herokuapp.com/rounds',
    'races': 'https://dev-snailx-api.herokuapp.com/races',
    'snails': 'https://dev-snailx-api.herokuapp.com/snails',
    'results': 'https://dev-snailx-api.herokuapp.com/results'
}

DB = {
    'host': "localhost",
    'user': "root",
    'password': "psqlpass",
    'database': "snailRacing",
    'port': "5432"
}


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-coded-key-pls-change'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://' + DB['user'] + ':' + DB[
        'password'] + '@' + DB['host'] + ':' + DB['port']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
