from feed import db
from feed.models.snail import Snail


def save(snail):
    db.session.add(snail)
    db.session.commit()


def find_one_by_id(id):
    response = Snail.query.get(id)

    return response
