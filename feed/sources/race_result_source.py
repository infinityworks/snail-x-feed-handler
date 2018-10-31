from feed import db
from feed.models.race_result import RaceResult


def save(race_result):
    db.session.add(race_result)
    db.session.commit()


# returns true if a race_result with the specified race_id exists in the db
def check_race_resulted(race_id):
    query = "SELECT race_result_id FROM raceresult WHERE race_id = '{}'".format(str(race_id))
    print("Query: " + query)
    query_result = db.engine.execute(query)
    result_exists = query_result.fetchone()

    print("Quuery result: " + str(result_exists))
    if result_exists:
        return True
    else:
        return False

def get_relevant_results(user_predictions):
    relevant_results = []
    for user_prediction in user_predictions:
        race_id = user_prediction[0]
        snail_id = user_prediction[1]
        query = "SELECT position FROM raceresult WHERE race_id = {} AND snail_id = {}".format(str(race_id), str(snail_id))
        query_result = db.engine.execute(query)
        result = query_result.fetchone()
        relevant_results.append(result)
    return relevant_results
