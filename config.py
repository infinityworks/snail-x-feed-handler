import os

URLS = {
    'auth': 'http://api.finiteworks.snailx.racing/auth/token',
    'rounds': 'http://api.finiteworks.snailx.racing/rounds',
    'races': 'http://api.finiteworks.snailx.racing/races',
    'snails': 'http://api.finiteworks.snailx.racing/snails',
    'results': 'http://api.finiteworks.snailx.racing/results'
}

# DB = {
#     'host': "localhost",
#     'user': "root",
#     'password': "psqlpass",
#     'database': "snailRacing",
#     'port': "5432"
# }

DB = {
    'host': "ec2-54-75-231-3.eu-west-1.compute.amazonaws.com",
    'user': "hlktjalicjrzic",
    'password': "de2f626a86d7c60b97e116a997795b5fe94065a1e7eaf7d3b399cd1d103dc55c",
    'database': "den6n9rjdut6sa",
    'port': "5432"
}

db_conn_str = "postgresql+psycopg2://" + DB['user'] + ':' + DB['password'] + '@' + DB['host'] + ':' + DB['port'] + "/" + DB['database']


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-coded-key-pls-change'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or db_conn_str
    SQLALCHEMY_TRACK_MODIFICATIONS = False
