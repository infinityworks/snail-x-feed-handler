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

