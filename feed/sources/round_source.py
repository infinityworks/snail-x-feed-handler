from feed import db
from feed.models.round import Round


def save(round):
    db.session.add(round)
    db.session.commit()


def find_one_by_id(id):
    return Round.query.get(id)
