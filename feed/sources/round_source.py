from feed import db
from feed.models import round


def save_round(round):
    session = db
    session.add(round)
    session.commit()

# def find_one_by_id(id):
#     return