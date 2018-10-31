from feed import db
from feed.models.race_result import RaceResult


def save(race_result):
    db.session.add(race_result)
    db.session.commit()

def get_round_user_ids(round_id):
    query = "SELECT DISTINCT user_id FROM racepredictions WHERE race_id IN (SELECT race_id FROM race WHERE round_id = {})".format(str(round_id))
    query_result = db.engine.execute(query)
    round_user_ids = query_result.fetchall()
    return round_user_ids

def get_predictions_by_user_id(user_id):
    query = "SELECT race_id, snail_id FROM racepredictions WHERE user_id = {}".format(str(user_id))
    query_result = db.engine.execute(query)
    user_predictions = query_result.fetchall()
    return user_predictions
