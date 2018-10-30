from feed import db
from feed.models.racecard import Racecard


def save(racecard):
    db.session.add(racecard)
    db.session.commit()


def find_one_by_id(id):
    return Racecard.query.get(id)

def check_racecard_exists(race_id):
    query = "SELECT race_card_id FROM racecard WHERE race_id = '{}'".format(str(race_id))
    query_result = db.engine.execute(query)
    result_exists = query_result.fetchone()
    return result_exists