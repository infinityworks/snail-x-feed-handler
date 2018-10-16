# from config import DB
# from flask import g
# from feed import app
# import psycopg2
#
#
# def get_db():
#     db = getattr(g, '_database', None)
#
#     if db is None:
#         db = g._database = connect_to_database()
#
#     return db
#
#
# @app.teardown_appcontext
# def teardown_db(teardown):
#     db = getattr(g, '_database', None)
#
#     if db is not None:
#         db.close()
#
#
# def connect_to_database():
#     return psycopg2.connect(
#         host=DB['host'],
#         user=DB['user'],
#         password=DB['password'],
#         database=DB['database']
#     )
