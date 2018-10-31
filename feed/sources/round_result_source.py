from feed import db
from feed.models.race_result import RaceResult


def save(round_result):
    db.session.add(round_result)
    db.session.commit()
