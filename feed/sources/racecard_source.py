from feed import db
from feed.models.round import Racecard


def save(racecard):
    db.session.add(racecard)
    db.session.commit()


def find_one_by_id(id):
    return Racecard.query.get(id)

def find_one_by_race_id_and_snail_id(race_id, snail_id):
