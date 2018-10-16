from feed import db
from feed.models import round


def save_round(round):
    db.session.add(round)
    db.session.commit()

# def find_one_by_id(id):
#     return