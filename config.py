import os

URLS = {
    'auth': 'https://dev-snailx-api.herokuapp.com/auth/token',
    'rounds': 'https://dev-snailx-api.herokuapp.com/rounds',
    'races': 'https://dev-snailx-api.herokuapp.com/races/',
    'snails': 'https://dev-snailx-api.herokuapp.com/snails/',
    'results': 'https://dev-snailx-api.herokuapp.com/results'
}

# DB = {
#     'host': "localhost",
#     'user': "root",
#     'password': "psqlpass",
#     'database': "snailRacing",
#     'port': "5432"
# }

DB = {
    'host': "ec2-23-21-147-71.compute-1.amazonaws.com",
    'user': "isfktaipxvnmbp",
    'password': "d3405d7dede20bc84142a6e336c8b476067decd768ac5ee13ccea55fa065b10c",
    'database': "d67lulaq5muhb8",
    'port': "5432"
}

db_conn_str = "postgresql+psycopg2://" + DB['user'] + ':' + DB['password'] + '@' + DB['host'] + ':' + DB['port'] + "/" + DB['database']


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-coded-key-pls-change'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or db_conn_str
    SQLALCHEMY_TRACK_MODIFICATIONS = False
