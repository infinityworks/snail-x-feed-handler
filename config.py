import os

URLS = {
    'auth': '/auth/token',
    'rounds': '/rounds',
    'races': '/races',
    'snails': '/snails',
    'results': '/results'
}

DB = {
    'host': "ec2-23-21-147-71.compute-1.amazonaws.com",
    'user': "isfktaipxvnmbp",
    'password': "d3405d7dede20bc84142a6e336c8b476067decd768ac5ee13ccea55fa065b10c",
    'database': "d67lulaq5muhb8"
}

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard-coded-key-pls-change'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
