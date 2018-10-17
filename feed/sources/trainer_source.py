from feed import db
from feed.models.trainer import Trainer


def save(trainer):
    db.session.add(trainer)
    db.session.commit()


def find_one_by_id(id):
    response = Trainer.query.get(id)

    return response
